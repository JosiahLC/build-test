from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    
    @app.route("/")
    def home():
        return "Hello World"
    
    return app
