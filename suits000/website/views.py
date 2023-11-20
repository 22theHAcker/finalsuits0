from flask import Blueprint, render_template, flash, request, jsonify, redirect, url_for
from flask_login import  login_required, current_user
from .models import Note, Suit
from . import db
import json

views = Blueprint('views', __name__)
def check_password(password):
    return password == "22"

@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Too short!', category = 'error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Tips added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

#CRUD
suits = Blueprint('suits', __name__)

@suits.route('/suits', methods=['GET'])
def get_all_suits():
    suits = Suit.query.all()
    return render_template("suits.html", suits=suits, user=current_user)

@suits.route('/suits/<int:suit_id>', methods=['GET'])
def get_suit(suit_id):
    suit = Suit.query.get(suit_id)
    return render_template("suit_detail.html", suit=suit, user=current_user)

@suits.route('/suits/add', methods=['GET', 'POST'])
@login_required
def add_suit():
    if request.method == 'POST':
        name = request.form.get('name')
        price = float(request.form.get('price'))
        color = request.form.get('color')
        size = request.form.get('size')

        new_suit = Suit(name=name, price=price, color=color, size=size)
        db.session.add(new_suit)
        db.session.commit()
        flash('Suit added!', category='success')
        return redirect(url_for('suits.get_all_suits'))

    return render_template("add_suit.html", user=current_user)

@suits.route('/suits/<int:suit_id>/update', methods=['GET', 'POST'])
@login_required
def update_suit(suit_id):
    suit = Suit.query.get(suit_id)

    if request.method == 'POST':
        password = request.form.get('password')

        if check_password(password):
            suit.name = request.form.get('name')
            suit.price = float(request.form.get('price'))
            suit.color = request.form.get('color')
            suit.size = request.form.get('size')

            db.session.commit()
            flash('Suit updated!', category='success')
            return redirect(url_for('suits.get_suit', suit_id=suit.id))
        else:
            flash('Incorrect password! Unable to update suit.', category='error')

    return render_template("update_suit.html", suit=suit, user=current_user)

    return redirect(url_for('suits.get_all_suits'))
