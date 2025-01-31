from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

res=0
@app.route('/')
def home():
    return "Hello, World!, This is a simple Flask API"

@app.route('/index')
def index():
    grupo="IDGS803"
    lista = ["Mario", "Pepe", "juan", 24, 25]
    return render_template("index.html",grupo= grupo, lista= lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    if request.method == "POST":
        num1 = request.form.get("n1")  
        num2 = request.form.get("n2") 
        res = int(num1) + int(num2)  
        return render_template("OperasBas.html", res=res)


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
    return f"El nombre es {nombre}"

@app.route("/foem1")
def foem1():
    return '''
        <form action="/submit" method="post">
            <label>Nombre</label>
            <input type="text" name="nombre" placeholder="pepe">
            <button type="submit">Enviar</button>
        </form>
    '''

@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):
    return f"La suma de {num1} + {num2} es {num1 + num2}"

if __name__ == '__main__':
    app.run(debug=True, port=3000)