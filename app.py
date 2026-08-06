from flask import Flask, render_template, request, redirect, url_for
from routes.upload_routes import upload_bp

app = Flask(__name__)
app.register_blueprint(upload_bp)

@app.route('/')
def input():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)