import json

from db import *


def create(json_str):
    json_fields = json.loads(json_str)
    restaurant_name = json_fields["restaurant_name"]
    manager_email = json_fields["manager_email"]
    region = json_fields["region"]
    address = json_fields["address"]
    serving_regions = json_fields["serving_regions"]
    work_hours = json_fields["work_hours"]
    delivery_time = json_fields["delivery_time"]
    delivery_fee = json_fields["delivery_fee"]

    query = 'INSERT INTO restaurant' \
            ' (name, manager_email, region, address, serving_regions, work_hours, delivery_time, delivery_fee)' \
            'VALUES (?,?,?,?,?,?,?,?)'
    fields = (restaurant_name, manager_email, region, address, serving_regions, work_hours, delivery_time, delivery_fee)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)
        db.commit()
        close_db()

        response = "restaurant registered successfully"
        return response

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR RESTAURANT REGISTRATION"
        return response


def update(json_str):
    json_fields = json.loads(json_str)
    restaurant_name = json_fields["restaurant_name"]
    manager_email = json_fields["manager_email"]
    region = json_fields["region"]
    address = json_fields["address"]
    serving_regions = json_fields["serving_regions"]
    work_hours = json_fields["work_hours"]
    delivery_time = json_fields["delivery_time"]
    delivery_fee = json_fields["delivery_fee"]

    query = 'UPDATE restaurant' \
            ' SET name=?, manager_email=?, region=?, address=?, serving_regions=?' \
            ', work_hours=?, delivery_time=?, delivery_fee=?)'
    fields = (restaurant_name, manager_email, region, address, serving_regions, work_hours, delivery_time, delivery_fee)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)
        db.commit()
        close_db()

        response = "restaurant update successfully"
        return response

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR UPDATE RESTAURANT"
        return response


def get_restaurant_by_name(restaurant_name):
    # json_fields = json.loads(json_str)
    #
    # restaurant_name = json_fields["name"]

    query = 'SELECT * FROM restaurant WHERE name=?'
    fields = (restaurant_name,)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)

        restaurants = cursor.fetchall()
        close_db()


    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR RESTAURANT GETTING"
        return response


def get_restaurant_by_region(region):
    # json_fields = json.loads(json_str)
    #
    # region = json_fields["region"]

    query = 'SELECT * FROM restaurant WHERE region=?'
    fields = (region,)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)

        restaurants = cursor.fetchall()
        close_db()


    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR RESTAURANT GETTING"
        return response


def delete(restaurant_name):
    # json_fields = json.loads(json_str)
    # restaurant_name = json_fields["restaurant_name"]

    query = 'DELETE restaurant WHERE name=?'
    fields = (restaurant_name,)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)
        db.commit()
        close_db()

        response = "restaurant deleted successfully"
        return response

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR DELETE RESTAURANT"
        return response
