import json

from db import *


def create(json_str):
    json_fields = json.loads(json_str)

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
    db = get_db()

    cursor = db.cursor()

    try:

        # checking to find out user not repetitive
        if len(get_user_by_phone_cursor(phone_number, cursor)) != 0:
            response = "USER ALREADY EXISTS !!!"
            return 'Error'

        # insert user
        cursor.execute(insert_query, fields)
        db.commit()
        close_db()
        response = "User registered successfully"
        return response

    except sqlite3.Error:  # I'm not sure the exact error that's raised by SQLite
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR USER REGISTRATION"
        return response


def update(json_str):
    json_fields = json.loads(json_str)

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
    db = get_db()
    cursor = db.cursor()

    try:
        # checking to find out user not repetitive
        if len(get_user_by_phone_cursor(phone_number, cursor)) == 0:
            response = "USER NOT EXISTS !!!"
            return

        # insert user
        cursor.execute(update_query, fields)
        db.commit()
        close_db()
        response = "User updated successfully"

    except sqlite3.Error:  # I'm not sure the exact error that's raised by SQLite
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR USER UPDATE DATA"


def delete(json_str):
    json_fields = json.loads(json_str)
    phone_number = json_fields["phone_number"]

    query = 'DELETE user WHERE phone_number=?'
    fields = (phone_number,)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)
        db.commit()
        close_db()

        response = "User deleted successfully"
        return response

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR DELETE USER"
        return response


def get_user_by_phone(json_str):
    json_fields = json.loads(json_str)

    entered_phone_num = json_fields["phone_number"]
    response = ""
    db = get_db()
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    try:
        user_rows = get_user_by_phone_cursor(entered_phone_num, cursor)
        if len(user_rows) == 0:
            response = "USER NOT EXIST !!!!"
        user_row = user_rows[0]

        user_row_dict = dict(user_row)
        close_db()

        return json.dumps(user_row_dict)

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR USER GET DATA"
        return response


def submit_order(json_str):
    json_fields = json.loads(json_str)
    user_phone_number = json_fields["phone_number"]
    restaurant_name = json_fields["restaurant"]
    food_name = json_fields["food"]
    count = json_fields["count"]

    response = ""
    db = get_db()
    cursor = db.cursor()

    try:
        cursor.execute("SELECT id FROM food WHERE name=?", (food_name,))
        food_id = cursor.fetchone()[0]

        insert_query = 'INSERT INTO f_order(user_phone, restaurant_name, food_id, count) VALUES (?,?,?,?)'

        cursor.execute(insert_query, (user_phone_number, restaurant_name, food_id, count))
        db.commit()

        close_db()

        response = "order registered successfully"
        return response
    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR ORDER REGISTRATION"
        return response


def get_favorite_foods_list(json_str):
    json_fields = json.loads(json_str)
    user_phone_number = json_fields["phone_number"]

    get_favorites_query = 'SELECT food.name, f_order.restaurant_name FROM' \
                          'comment INNER JOIN f_order ON comment.order_id = f_order.id' \
                          'INNER JOIN food ON f_order.food_id = food.id' \
                          'WHERE user_phone=?' \
                          'GROUP BY food.name, f_order.restaurant_name' \
                          'HAVING AVG(comment.score) > 3 OR COUNT(*) > 5'
    response = ""
    db = get_db()
    cursor = db.cursor()

    try:
        cursor.execute(get_favorites_query, (user_phone_number,))
        favorites_list = cursor.fetchall()

        close_db()

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN GET FAVORITES LIST"
        return response


def get_orders_history(json_str):
    json_fields = json.loads(json_str)
    user_phone_number = json_fields["phone_number"]

    order_select_query = 'SELECT f_order.id, food.name, f_order.restaurant_name, f_order.count, f_order.status, ' \
                         'f_order.date' \
                         'FROM f_order INNER JOIN BY food ON f_order.food_id=food.id' \
                         'WHERE user_phone = ?'
    response = ""
    db = get_db()
    cursor = db.cursor()

    try:
        cursor.execute(order_select_query, (user_phone_number,))
        order_list = cursor.fetchall()

        close_db()

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN GET ORDERS LIST"
        return response


def get_user_by_phone_cursor(phone_number, cursor):
    select_query = 'SELECT * FROM user WHERE phone_number=?'
    cursor.execute(select_query, (phone_number,))
    users = cursor.fetchall()
    print('users : ' + str(users))
    return users
