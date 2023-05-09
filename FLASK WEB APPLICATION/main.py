from website import create_app, config

app = create_app()

if __name__ == "__main__":

    with app.app_context():
        app.config['home'] = config.Home(config.rooms)
        app.run(debug=True, host="0.0.0.0")
    