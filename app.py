from flask import Flask, render_template
from routes.upload_routes import upload_bp
from routes.summary_routes import summary_bp
from routes.chat_routes import chat_bp
import config


app = Flask(__name__)
app.register_blueprint(upload_bp)
app.register_blueprint(summary_bp)
app.register_blueprint(chat_bp)

@app.route('/')
def input():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

app.config['SECRET_KEY'] = config.SECRET_KEY

if __name__ == '__main__':
    app.run(debug=True)