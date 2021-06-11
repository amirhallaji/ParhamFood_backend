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
    pass


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
    select_query = 'SELECT email FROM manager'
    cursor.execute(select_query)
    emails = cursor.fetchall()
    for e in emails:
        if e[0] == email:
            return True
    return False
