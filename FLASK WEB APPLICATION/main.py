from website import create_app, config
from flask_socketio import SocketIO


app = create_app()
socketio = SocketIO(app)


if __name__ == "__main__":

    # with app.app_context():
    #     # config.mainConfig()
    #     # config.testBehavior()
    #     app.run(debug=True, host="0.0.0.0")
    socketio.run(app, debug=True, host="0.0.0.0")
    