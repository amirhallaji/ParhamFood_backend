import json

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
        if len(get_manager_by_email(email, cursor)) != 0:
            response = "MANAGER ALREADY EXISTS!"
            return

        cursor.execute(query, fields)
        cursor.commit()
        close_db()
        response = "Manager registered successfully"

    except sqlite3.IntegrityError:  # I'm not sure the exact error that's raised by SQLite
        close_db()
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
        if len(get_manager_by_email(email, cursor)) == 0:
            response = "MANAGER NOT EXISTS!"
            return

        cursor.execute(query, fields)
        cursor.commit()
        close_db()
        response = "Manager updated successfully"

    except sqlite3.IntegrityError:  # I'm not sure the exact error that's raised by SQLite
        close_db()
        response = "A PROBLEM ACCRUED IN MANAGER UPDATE"


def get(json_fields):
    entered_email = json_fields["email"]
    entered_pass = json_fields["password"]
    response = ""
    db = get_db()
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    try:
        manager_rows = get_manager_by_email(entered_email, cursor)
        if len(manager_rows) == 0:
            response = "MANAGER NOT EXIST !!!!"
        manager_row = manager_rows[0]

        if manager_row["password"] != entered_pass:
            response = "INCORRECT PASSWORD"
            return

        manager_row_dict = dict(manager_row)
        del manager_row_dict["email"]
        del manager_row_dict["password"]

        return json.dumps(manager_row_dict)

    except sqlite3.Error:
        response = "WE HAVE A PROBLEM IN DATABASE FOR MANAGER GET DATA"
        return


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


def get_manager_by_email(email, cursor):
    select_query = 'SELECT * FROM manager WHERE email = ?'
    cursor.execute(select_query, (email,))
    managers = cursor.fetchall()
    return managers
