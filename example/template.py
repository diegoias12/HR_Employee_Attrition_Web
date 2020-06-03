from flask import Flask
from flask import render_template

# app = Flask(__name__, template_folder='template')
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index_nombre(name='Diego'):
    my_list = [3, 5, 1, 9, 6, 7]
    return render_template('home.html', nombre=name, my_list=my_list)

if __name__ == '__main__':
    app.run(debug=True, port=8000)