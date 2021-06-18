import json

from db import *


def create(json):
    pass


def update(json):
    pass


def get(json):
    pass


def delete(json):
    pass


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
