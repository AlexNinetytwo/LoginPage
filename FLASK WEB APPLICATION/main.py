from website import create_app, config


app = create_app()


if __name__ == "__main__":

    with app.app_context():
        config.mainConfig()
        app.config['home'] = config.House(config.groundFloor)
        app.config['home'].addRooms(config.firstFloor,"1.OG",1)
        app.run(debug=True, host="0.0.0.0")
    