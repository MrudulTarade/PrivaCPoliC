from fileinput import filename
from flask import *
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(filename)
            return redirect(url_for('display', filename=filename))
    return render_template('templates\\upload.html')

if __name__ == '__main__':
    app.run(debug=True)