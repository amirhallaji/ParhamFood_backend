import json

from db import *


# create
def submit_comment(json_str):
    json_fields = json.loads(json_str)
    order_id = json_fields["order_id"]
    score = json_fields["score"]
    content = json_fields["content"]

    response = ""
    db = get_db()
    cursor = db.cursor()

    try:
        cursor.execute('INSERT INTO comment(order_id, score, content) VALUES (?,?,?)', (order_id, score, content))
        db.commit()

        close_db()
        response = "comment registered successfully"
        return response
    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR COMMENT REGISTRATION"
        return response


def update_by_user(json_str):
    json_fields = json.loads(json_str)

    order_id = json_fields["order_id"]
    score = json_fields["score"]
    content = json_fields["content"]

    query = 'UPDATE comment SET score=?, content=? WHERE order_id=?'
    fields = (score, content, order_id)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)
        db.commit()
        close_db()

        response = "Comment updated by user successfully"
        return response

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR COMMENT UPDATE BY USER"
        return response


# or reply to a comment
def update_by_manager(json_str):
    json_fields = json.loads(json_str)

    order_id = json_fields["order_id"]
    manager_reply = json_fields["manager_reply"]

    query = 'UPDATE comment SET manager_reply=? WHERE order_id=?'
    fields = (manager_reply, order_id)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)
        db.commit()
        close_db()

        response = "Comment updated by user successfully"
        return response

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR COMMENT UPDATE BY USER"
        return response


def get_by_order_id(order_id):
    # json_fields = json.loads(json_str)
    #
    # order_id = json_fields["order_id"]

    query = 'SELECT score, content, manager_reply FROM comment WHERE order_id=?'
    fields = (order_id,)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)

        comment = cursor.fetchone()

        close_db()

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR GETTING COMMENT WITH ORDER_ID"
        return response


def delete(order_id):
    # json_fields = json.loads(json_str)
    # order_id = json_fields["order_id"]

    query = 'DELETE comment WHERE order_id=?'
    fields = (order_id,)

    response = ""
    db = get_db()

    cursor = db.cursor()

    try:

        cursor.execute(query, fields)
        db.commit()
        close_db()

        response = "Comment Deleted successfully"
        return response

    except sqlite3.Error:
        close_db()
        response = "WE HAVE A PROBLEM IN DATABASE FOR IN DELETE COMMENT"
        return response
