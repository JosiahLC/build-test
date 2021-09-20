from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    
    @app.route("/",  methods=["GET"])
    def home():
        return render_template("home.html")
    
    return app
