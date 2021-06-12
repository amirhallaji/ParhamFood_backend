from db import *


def create(json):
    email = json["email"]
    password = json["password"]
    name = json["name"]

    query = 'INSERT INTO manager (email, password, name) ' \
            'VALUES (?, ?, ?)'
    fields = (email, password, name)

    response = ""
    cursor = get_db().cursor()

    try:
        if is_manager_exist(email, cursor):
            response = "MANAGER ALREADY EXISTS!"
            return

        cursor.execute(query, fields)
        cursor.commit()
        response = "Manager registered successfully"

    except sqlite3.IntegrityError:  # I'm not sure the exact error that's raised by SQLite
        response = "A PROBLEM ACCRUED IN MANAGER CREATION"


def update(json):
    email = json["email"]
    password = json["password"]
    name = json["name"]

    query = 'UPDATE manager SET password=?, name=? ' \
            'WHERE email=?'
    fields = (password, name, email)

    response = ""
    cursor = get_db().cursor()

    try:
        if not is_manager_exist(email, cursor):
            response = "MANAGER NOT EXISTS!"
            return

        cursor.execute(query, fields)
        cursor.commit()
        response = "Manager updated successfully"

    except sqlite3.IntegrityError:  # I'm not sure the exact error that's raised by SQLite
        response = "A PROBLEM ACCRUED IN MANAGER UPDATE"


def get(json):
    pass


def addFood(json):
    pass


def removeFood(json):
    pass


def disableFood(json):
    pass


def acceptOrder(json):
    pass


def replyToComment(json):
    pass


def is_manager_exist(email, cursor):
    select_query = 'SELECT email FROM manager WHERE email = ?'
    cursor.execute(select_query, (email,))
    emails = cursor.fetchall()

    if len(emails) == 0:
        return True

    return False
