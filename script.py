from flask import Flask
from flask import render_template
from flask import request

from prediction import make_prediction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        form_dict = request.form
        result = make_prediction(form_dict)
        return render_template('result.html', result = form_dict, proba = result)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
