from fileinput import filename
from flask import *
from werkzeug.utils import secure_filename
from services.pdf_reader import extract_text
from services.preprocessing import clean_text, advanced_preprocessing

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(filename)
            cleaned_text = clean_text(filename)
            processed_text = advanced_preprocessing(cleaned_text)
            return redirect(url_for('display', filename=filename, processed_text=processed_text))
    return render_template('templates\\summary.html')

if __name__ == '__main__':
    app.run(debug=True)