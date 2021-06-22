import json

from db import *


def create(json_str):
    json_fields = json.loads(json_str)

    email = json_fields["email"]
    password = json_fields["password"]
    name = json_fields["name"]

    query = 'INSERT INTO manager (email, password, name) ' \
            'VALUES (?, ?, ?)'
    fields = (email, password, name)

    response = ""
    db = get_db()
    cursor = db.cursor()

    try:
        if len(get_manager_by_email(email, cursor)) != 0:
            response = "MANAGER ALREADY EXISTS!"
            return

        cursor.execute(query, fields)
        db.commit()
        close_db()
        response = "Manager registered successfully"

    except sqlite3.IntegrityError:  # I'm not sure the exact error that's raised by SQLite
        close_db()
        response = "A PROBLEM ACCRUED IN MANAGER CREATION"


def update(json_str):
    json_fields = json.loads(json_str)

    email = json_fields["email"]
    password = json_fields["password"]
    name = json_fields["name"]

    query = 'UPDATE manager SET password=?, name=? ' \
            'WHERE email=?'
    fields = (password, name, email)

    response = ""
    db = get_db()
    cursor = db.cursor()

    try:
        if len(get_manager_by_email(email, cursor)) == 0:
            response = "MANAGER NOT EXISTS!"
            return

        cursor.execute(query, fields)
        db.commit()
        close_db()
        response = "Manager updated successfully"

    except sqlite3.IntegrityError:  # I'm not sure the exact error that's raised by SQLite
        close_db()
        response = "A PROBLEM ACCRUED IN MANAGER UPDATE"


def get_by_email(entered_email):
    # json_fields = json.loads(json_str)

    # entered_email = json_fields["email"]
    response = ""
    db = get_db()
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    try:
        manager_rows = get_manager_by_email(entered_email, cursor)
        if len(manager_rows) == 0:
            response = "MANAGER NOT EXIST !!!!"
        manager_row = manager_rows[0]

        manager_row_dict = dict(manager_row)

        close_db()
        return json.dumps(manager_row_dict)

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR MANAGER GET DATA"
        return


def get_related_comments(email):
    # json_fields = json.loads(json_str)
    #
    # email = json_fields["email"]

    query = 'SELECT score, content, manager_reply FROM comment INNER JOIN f_order' \
            'ON f_order.id = comment.order_id INNER JOIN restaurant' \
            'ON restaurant_food.restaurant_name = restaurant.name' \
            ' WHERE restaurant.manager_email=?'
    fields = (email,)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)

        comments = cursor.fetchall()

        close_db()

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR COMMENT GETTING BY MANAGER email"
        return response


def get_manager_by_email(email, cursor):
    select_query = 'SELECT * FROM manager WHERE email = ?'
    cursor.execute(select_query, (email,))
    managers = cursor.fetchall()
    return managers
