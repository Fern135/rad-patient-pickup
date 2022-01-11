from app import create_app, Config

app = create_app()

if __name__ == '__main__':
    app.run(
        threaded=True,  # to handle multiple requests at the same time
        debug=Config.DEBUG,
        port=Config.port,
        host=Config.apphost  # run online of my own computer
    )