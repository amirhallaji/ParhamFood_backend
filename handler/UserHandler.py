import json

from db import *


def create(json_fields):
    phone_number = json_fields["phone_number"]
    password = json_fields["password"]
    name = json_fields["name"]
    region = json_fields["region"]
    address = json_fields["address"]
    credit = 1000000  # 1,000,000

    insert_query = 'INSERT INTO user (phone_number, password, name, region, address, credit) ' \
                   'VALUES (?, ?, ?, ?, ?, ?)'
    fields = (phone_number, password, name, region, address, credit)

    response = ""
    cursor = get_db().cursor()

    try:
        # checking to find out user not repetitive
        if len(get_user_by_phone(phone_number, cursor)) != 0:
            response = "USER ALREADY EXISTS !!!"
            return

        # insert user
        cursor.execute(insert_query, fields)
        cursor.commit()
        close_db()
        response = "User registered successfully"

    except sqlite3.Error:  # I'm not sure the exact error that's raised by SQLite
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR USER REGISTRATION"


def update(json_fields):
    phone_number = json_fields["phone_number"]
    password = json_fields["password"]
    name = json_fields["name"]
    region = json_fields["region"]
    address = json_fields["address"]
    credit = json_fields["credit"]

    update_query = 'UPDATE user SET password=?, name=?, region=?, address=?, credit=? ' \
                   'WHERE phone_number=?'
    fields = (password, name, region, address, credit, phone_number)

    response = ""
    cursor = get_db().cursor()

    try:
        # checking to find out user not repetitive
        if len(get_user_by_phone(phone_number, cursor)) == 0:
            response = "USER NOT EXISTS !!!"
            return

        # insert user
        cursor.execute(update_query, fields)
        cursor.commit()
        close_db()
        response = "User updated successfully"

    except sqlite3.Error:  # I'm not sure the exact error that's raised by SQLite
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR USER UPDATE DATA"


def get(json_fields):
    entered_phone_num = json_fields["phone_number"]
    entered_pass = json_fields["password"]
    response = ""
    db = get_db()
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    try:
        user_rows = get_user_by_phone(entered_phone_num, cursor)
        if len(user_rows) == 0:
            response = "USER NOT EXIST !!!!"
        user_row = user_rows[0]

        if user_row["password"] != entered_pass :
            response = "INCORRECT PASSWORD"
            return

        user_row_dict = dict(user_row)
        del user_row_dict["phone_number"]
        del user_row_dict["password"]

        return json.dumps(user_row_dict)

    except sqlite3.Error:
        response = "WE HAVE A PROBLEM IN DATABASE FOR USER GET DATA"
        return


def order(json):
    pass


def submitComment(json):
    pass


def getFavoriteFoodsList(json):
    pass


def getOrdersHistory(json):
    pass


def get_user_by_phone(phone_number, cursor):
    select_query = 'SELECT * FROM user WHERE phone_number = ?'
    cursor.execute(select_query, (phone_number, ))
    users = cursor.fetchall()
    return users
