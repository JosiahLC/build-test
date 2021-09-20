from flask import Flask, render_template, request, redirect

def create_app():
    app = Flask(__name__)
    
    db = SQLAlchemy()
    
    db.init_app(app)
    
    @app.route("/")
    def hello_world():
        return render_template("index.html")
    
    return app
