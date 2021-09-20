from flask import Flask

def create_app():
    app = Flask(__name__)
    
    db.init_app(app)
    
    @app.route("/")
    def hello_world():
        return "Hello World"
    
    return app
