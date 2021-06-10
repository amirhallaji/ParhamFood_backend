
from ParhamFood_backend.db import *
from flask import flash


def create(json):
    phone_number    = json["phone_number"]
    password        = json["password"]
    name            = json["name"]
    region          = json["region"]
    address         = json["address"]
    credit          = 1000000               # 1,000,000

    db = get_db()
    error = None

    if phone_number is None:
        error = 'Phone Number is required.'
    elif password is None:
        error = 'Password is required.'

    if error is not None:
        flash(error)
    else:
        db = get_db()
        db.execute(
            'INSERT INTO user (phone_number, password, name, region, address, credit)'
            ' VALUES (?, ?, ?, ?, ?, ?)',
            (phone_number, password, name, region, address, credit)
        )
        db.commit()


def update(json):
    pass


def get(json):
    pass


def order(json):
    pass


def submitComment(json):
    pass


def getFavoriteFoodsList(json):
    pass


def getOrdersHistory(json):
    pass

