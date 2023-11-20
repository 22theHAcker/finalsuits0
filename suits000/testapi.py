from flask import request

BASE = "http://127.0.0.1:5000/"

responce = request.get(BASE + "api")
print(responce.json())