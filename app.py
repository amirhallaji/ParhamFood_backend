
from flask import Flask
from flask_socketio import SocketIO
from markupsafe import escape
import os


# import other .py files
import ParhamFood_backend.handler.ManagerHandler as MH
import ParhamFood_backend.handler.UserHandler as UH
import ParhamFood_backend.handler.RestaurantHandler as RH
import ParhamFood_backend.db as db


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
)

app.config.from_pyfile('config.py', silent=True)
db.init_app(app)

socketio = SocketIO(app)


@app.route("/")
def hello_world():
    return "Hello World!"


# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"


# --------------------------------------------------------------------
#                           USER EVENTS
# --------------------------------------------------------------------
@socketio.on('create user')
def handle_create_user(json):
    response = UH.create(json)
    # print('received my event: ' + str(json))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('update user')
def handle_update_user(json):
    response = UH.update(json)
    # print('received my event: ' + str(json))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('make order')
def handle_make_order(json):
    response = UH.order(json)
    # print('received my event: ' + str(json))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('submit comment')
def handle_submit_comment(json):
    response = UH.submitComment(json)
    # print('received my event: ' + str(json))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('get favorite foods list')
def handle_get_favorite_foods_list(json):
    response = UH.getFavoriteFoodsList(json)
    # print('received my event: ' + str(json))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('get orders history')
def handle_get_orders_history(json):
    response = UH.getOrdersHistory(json)
    # print('received my event: ' + str(json))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)



# --------------------------------------------------------------------
#                           MANAGER EVENTS
# --------------------------------------------------------------------
@socketio.on('create manager')
def handle_create_manager(json):
    response = MH.create(json)
    # print('received my event: ' + str(json))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('update manager')
def handle_update_manager(json):
    response = MH.update(json)
    # print('received my event: ' + str(json))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('add food')
def handle_add_food(json):
    response = MH.addFood(json)
    # print('received my event: ' + str(json))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('remove food')
def handle_remove_food(json):
    response = MH.removeFood(json)
    # print('received my event: ' + str(json))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('disable food')
def handle_disable_food(json):
    response = MH.disableFood(json)
    # print('received my event: ' + str(json))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('accept order')
def handle_accept_order(json):
    response = MH.acceptOrder(json)
    # print('received my event: ' + str(json))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


@socketio.on('reply to comment')
def handle_reply_to_comment(json):
    response = MH.replyToComment(json)
    # print('received my event: ' + str(json))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


# --------------------------------------------------------------------
#                           RESTAURANT EVENTS
# --------------------------------------------------------------------
@socketio.on('create restaurant')
def handle_create_restaurant(json):
    response = RH.create(json)
    # print('received my event: ' + str(json))
    # response = {
    #     "status_code" : "200"
    # }
    socketio.emit('my response', response)


if __name__ == '__main__':
    socketio.run(app)
