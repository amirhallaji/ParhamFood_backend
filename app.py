
from flask import Flask
from flask_socketio import SocketIO
from markupsafe import escape
import os
import json


# import other .py files
import handler.ManagerHandler as MH
import handler.UserHandler as UH
import handler.RestaurantHandler as RH
import handler.FoodHandler as FH
import handler.CommentHandler as CH
import db as db


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
)

app.config.from_pyfile('config.py', silent=True)
db.init_app(app)

socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def sayHello():
    return 'Hello!'

@app.route("/create")
def createUser():
    res = handle_create_user()
    return res

@app.route("/get")
def getUser():
    res = handle_get_user()
    return res


# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

# --------------------------------------------------------------------
#                           TEST
# --------------------------------------------------------------------

@socketio.on('give me user name')
def handle_testtt():
    print('message received')
    socketio.emit('get user name', 'alireza mohammadi')
    print('message sent')

# --------------------------------------------------------------------
#                           USER EVENTS
# --------------------------------------------------------------------
@socketio.on('create user')
def handle_create_user(json_req):

    print(json_req)
    return

    # dictt = {
    #     'phone_number': '333',
    #     'password' : '123@',
    #     'name' : 'ali',
    #     'region' : '1',
    #     'address' : 'velenjak',
    # }

    json_req = ''
    # json_req = json.dumps(dictt)

    response = UH.create(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    # socketio.emit('my response', response)
    # print(response)

    return response


@socketio.on('test_server')
def handle_test():
    print('test function')
    socketio.send('message', 'amir')
    socketio.emit('test_client', 'amir')


@socketio.on('message')
def handle_test_msg(msg):
    print('test msg function')
    socketio.send(msg, broadcast=True)
    return None


@socketio.on('update user')
def handle_update_user(json_req):
    response = UH.update(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('get user')
def handle_get_user():

    # dictt = {
    #     'phone_number': '333',
    #     'password': '123@'
    # }

    json_req = ''
    # json_req = json.dumps(dictt)

    response = UH.get_user_by_phone(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    # socketio.emit('my response', response)
    # print(response)

    return response


@socketio.on('make order')
def handle_make_order(json_req):

    """
        phone_number
        restaurant_name
        food
        count
    """

    response = UH.submit_order(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('submit comment')
def handle_submit_comment(json_req):
    response = UH.submit_comment(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('get favorite foods list')
def handle_get_favorite_foods_list(json_req):
    response = UH.get_favorite_foods_list(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('get orders history')
def handle_get_orders_history(json_req):
    response = UH.get_orders_history(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)



# --------------------------------------------------------------------
#                           MANAGER EVENTS
# --------------------------------------------------------------------
@socketio.on('create manager')
def handle_create_manager(json_req):
    response = MH.create(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('update manager')
def handle_update_manager(json_req):
    response = MH.update(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('get manager')
def handle_get_manager(json_req):
    response = MH.get_by_email(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('add food')
def handle_add_food(json_req):
    print('received')
    response = FH.create_food(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('get food from manager', json_req)
    print(response)


@socketio.on('remove food')
def handle_remove_food(json_req):
    response = MH.removeFood(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('disable food')
def handle_disable_food(json_req):
    response = MH.disableFood(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('accept order')
def handle_accept_order(json_req):
    response = MH.acceptOrder(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('reply to comment')
def handle_reply_to_comment(json_req):
    response = MH.replyToComment(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


# --------------------------------------------------------------------
#                           RESTAURANT EVENTS
# --------------------------------------------------------------------
@socketio.on('create restaurant')
def handle_create_restaurant(json_req):
    response = RH.create(json_req)
    # print('received my event: ' + str(json_req))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)



# --------------------------------------------------------------------
#                           FOOD EVENTS
# --------------------------------------------------------------------
@socketio.on('add food ')
def handle_create_restaurant(json_req):
    response = FH.get_by_food_name(json_req)
    socketio.emit('search result page - get foods', response)


if __name__ == '__main__':
    socketio.run(app, port=4001)
