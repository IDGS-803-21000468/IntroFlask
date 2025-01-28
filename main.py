from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!, This is a simple Flask API"

@app.route('/hola')
def hola():
    return "Hola, Mundo!, Este es un simple API con Flask"

@app.route('/user/<string:user>')
def saludo(user):
    return f"¡Hola {user}!, ¿Cómo estás?"

@app.route('/user/<string:user>/edad/<int:edad>')
def saludo_con_edad(user, edad):
    return jsonify(message=f"¡Hola {user}!, ¿Cómo estás?, veo que tienes {edad} años")

@app.route("/default")
@app.route("/default/<string:nombre>")
def default(nombre="pedro"):
    return f"El nombre es  {nombre}"


@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):
    return f"La suma de {num1} + {num2} es {num1 + num2}"

if __name__ == '__main__':
    app.run(debug=True,port=3000)

