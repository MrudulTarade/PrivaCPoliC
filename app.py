from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello World"

@app.route("/")
def homepage():
    return "Welcome to the homepage!"

if __name__ == "__main__":
    app.run(debug=True)