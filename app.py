from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('home.html')

@app.route('/passing', methods = ['GET', 'POST'])
def display():
    if request.method == 'POST':
        result = request.form
        return render_template(
            'results_data.html',
            result = result
        )

if __name__ == '__main__':
    app.run(debug=True)