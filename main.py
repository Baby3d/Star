from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome home!"



@app.route("/about")
def about():
    return "<h1> Welcome </h1>"


app.run(debug=True)