from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo, nuevo cambio'

# http://127.0.0.1:8000/params?nombre=Diego&apellido=Alcantara
"""
@app.route('/params')
def params(name='No_nombre', apellido='No_apellido'):
    nombre = request.args.get('nombre', 'No hay nombre')
    apellido = request.args.get('apellido', 'No hay apellido')
    return 'Tu nombre es: {} {}'.format(nombre, apellido)
"""

@app.route('/params')
@app.route('/params/<name>')
@app.route('/params/<name>/<int:num>')
def params(name='No_nombre', num='No_apellido'):
    return 'Tu nombre es: {} {}'.format(name, num)

if __name__ == '__main__':
    app.run(debug=True, port=8000)