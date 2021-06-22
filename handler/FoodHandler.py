import json

from db import *


def create_food(json_str):
    json_fields = json.loads(json_str)

    food_name = json_fields["food_name"]
    restaurant_name = json_fields["restaurant_name"]
    count = json_fields["count"]
    copen_type = json_fields["copen_type"]
    price = json_fields["price"]
    disabled = json_fields["disabled"]

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute('INSERT food (name) VALUES (?)', (food_name))
        db.commit()
        food_id = cursor.lastrowid
        query = 'INSERT INTO restaurant_food(restaurant_name, food_id, count, copen_type, price, disabled)' \
                'VALUES (?,?,?,?,?,?)'
        fields = (restaurant_name, food_id, count, copen_type, price, disabled)

        cursor.execute(query, fields)
        db.commit()

        close_db()

        response = "food registered successfully"
        return response

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR FOOD REGISTRATION"
        return response


def update_food_name(json_str):
    json_fields = json.loads(json_str)

    food_id = json_fields["food_id"]
    food_name = json_fields["food_name"]

    query = 'UPDATE food SET name=? WHERE id=?'
    fields = (food_name, food_id)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)
        db.commit()
        close_db()

        response = "food name updated successfully"
        return response

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR FOOD NAME UPDATE"
        return response


def update_food_information(json_str):
    json_fields = json.loads(json_str)

    food_id = json_fields["food_id"]
    restaurant_name = json_fields["restaurant_name"]
    count = json_fields["count"]
    copen_type = json_fields["copen_type"]
    price = json_fields["price"]
    disabled = json_fields["disabled"]

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:
        query = 'UPDATE restaurant_food SET restaurant_name=?, count=?, copen_type=?, price=?, disabled=? WHERE ' \
                'food_id=? '
        fields = (restaurant_name, count, copen_type, price, disabled, food_id)

        cursor.execute(query, fields)
        db.commit()

        close_db()

        response = "food information updated successfully"
        return response

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR FOOD INFORMATION UPDATE"
        return response


def get_by_food_restaurant(json_str):
    json_fields = json.loads(json_str)

    food_name = json_fields["food_name"]
    restaurant_name = json_fields["restaurant_name"]

    query = 'SELECT food_id, food.name, restaurant_name, count, copen_type, price, disabled' \
            'FROM food_restaurant INNER JOIN ON food.id = food_restaurant.food_id' \
            'WHERE food.name=? AND restaurant_name=?'
    fields = (food_name, restaurant_name)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)

        foods = cursor.fetchall()
        close_db()


    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR FOOD GETTING BY FOOD AND RESTAURANT NAME"
        return response


def get_by_food_name(food_name):
    # json_fields = json.loads(json_str)
    #
    # food_name = json_fields["food_name"]

    query = 'SELECT food_id, food.name, restaurant_name, count, copen_type, price, disabled' \
            'FROM food_restaurant INNER JOIN ON food.id = food_restaurant.food_id' \
            'WHERE food.name=?'
    fields = (food_name,)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)

        foods = cursor.fetchall()
        close_db()


    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR FOOD GETTING BY FOOD NAME"
        return response


def get_by_restaurant(restaurant_name):
    # json_fields = json.loads(json_str)
    #
    # restaurant_name = json_fields["restaurant_name"]

    query = 'SELECT food_id, food.name, restaurant_name, count, copen_type, price, disabled' \
            'FROM food_restaurant INNER JOIN ON food.id = food_restaurant.food_id' \
            'WHERE restaurant_name=?'
    fields = (restaurant_name, )

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)

        foods = cursor.fetchall()
        close_db()


    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR FOOD GETTING BY RESTAURANT NAME"
        return response


def delete_food(food_id):
    # json_fields = json.loads(json_str)
    #
    # food_id = json_fields["food_id"]

    query = 'DELETE food WHERE id=?'
    fields = (food_id, )

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)
        db.commit()
        close_db()

        response = "food deleted successfully"
        return response

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR DELETE FOOD"
        return response


def get_food_comments(json_str):
    json_fields = json.loads(json_str)
    food_name = json_fields["food"]
    restaurant_name = json_fields["restaurant"]

    query = 'SELECT score, content, manager_reply FROM comment INNER JOIN f_order' \
            'ON f_order.id = comment.order_id INNER JOIN restaurant_food' \
            'ON restaurant_food.food_id = f_order.food_id INNER JOIN food' \
            'ON f_order.food_id = food.id WHERE food.name=? AND restaurant_food.restaurant_name=?'
    fields = (food_name, restaurant_name)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)
        comments = cursor.fetchall()

        close_db()

        response = "comments fetched successfully"


    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR FOOD COMMENT GETTING"
        return response
