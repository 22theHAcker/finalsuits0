# # from flask_sqlalchemy import SQLAlchemy
# # from website import create_app, db
# #
# # from website.models import Suit
# # app = create_app()
# #
# # # with app.app_context():
# # #     business_suits_data = [
# # #         {"name": "Classic Fit Suit", "color": "Black", "price": 159.99, "imageUrl": "suits/suit1.jpg"},
# # #         {"name": "Notch Lapel", "color": "Black", "price": 199.99, "imageUrl": "suits/suit2.jpg"},
# # #         {"name": "Single-Breasted Suit", "color": "Navy Blue", "price": 139.99, "imageUrl": "suits/suit3.jpg"},
# # #         {"name": "Unstructured Business Suit", "color": "Dark Grey", "price": 199.99, "imageUrl": "suits/suit4.jpg"},
# # #     ]
# # #
# # #     for suit_data in business_suits_data:
# # #         new_suit = Suit(**suit_data)
# # #         db.session.add(new_suit)
# #
# #     # db.session.commit()
#
#
from flask_sqlalchemy import SQLAlchemy
from website import create_app, db
from website.models import Shoes
from .models import db

app = create_app()

with app.app_context():
    shoes_data = [
        {"name": "Classic Tracker", "price": 59.99, "imageUrl": "shoes/shoe1.jpg"},
        {"name": "Full Winter", "price": 49.99, "imageUrl": "shoes/shoe2.jpg"},
        {"name": "Spring South",  "price": 69.99, "imageUrl": "shoes/shoe3.jpg"},
        {"name": "Loronat Aziza",  "price": 109.99, "imageUrl": "shoes/shoe4.jpg"},
        {"name": "Brown Horse", "price": 59.99, "imageUrl": "shoes/shoe5.jpg"},
        {"name": "Dance Hall", "price": 89.99, "imageUrl": "shoes/shoe6.jpg"},
        {"name": "Wood Myth",  "price": 59.99, "imageUrl": "shoes/shoe7.jpg"},
        {"name": "Ferrari Style", "price": 79.99, "imageUrl": "shoes/shoe8.jpg"},
        {"name": "Cowboy Style", "price": 89.99, "imageUrl": "shoes/shoe9.jpg"},
    ]

    for shoe_data in shoes_data:
        new_shoe = Shoes(**shoe_data)
        db.session.add(new_shoe)

    db.session.commit()