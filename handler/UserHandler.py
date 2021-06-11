from db import *
from flask import flash


def create(json):
    phone_number = json["phone_number"]
    password = json["password"]
    name = json["name"]
    region = json["region"]
    address = json["address"]
    credit = 1000000  # 1,000,000

    insert_query = 'INSERT INTO user (phone_number, password, name, region, address, credit) ' \
                   'VALUES (?, ?, ?, ?, ?, ?)'
    fields = (phone_number, password, name, region, address, credit)

    response = ""
    cursor = get_db().cursor()

    try:
        # checking to find out user not repetitive
        if is_user_exist(phone_number, cursor):
            response = "USER ALREADY EXISTS !!!"

        # insert user
        cursor.execute(insert_query, fields)
        cursor.commit()
        response = "User registered successfully"

    except sqlite3.Error:  # I'm not sure the exact error that's raised by SQLite
        response = "WE HAVE A PROBLEM IN DATABASE FOR USER REGISTRATION"


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


def is_user_exist(phone_number, cursor):
    select_query = 'SELECT phone_number FROM user WHERE phone_number = ?'
    cursor.execute(select_query, (phone_number, ))
    phone_numbers = cursor.fetchall()
    if len(phone_numbers) == 0:
        return True
    return False
