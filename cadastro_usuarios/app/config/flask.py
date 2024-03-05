from flask import Flask



def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    return app

def run_app():
    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')


