from flask import Flask, request, jsonify, render_template, redirect, url_for
from forms import UseForm
from flask import g
from flask import flash
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key="1234567"
csrf = CSRFProtect(app)
res=0


@app.errorhandler(404)
def page_not_found(e):
    return render_template("400.html"), 404

@app.before_request
def before_request():
    g.nombre = "Pedro"
    print("Before request 1")

@app.after_request
def after_request(response):
    print("after request 2")
    return response

@app.route('/')
def home():
    lista = {"betillo", "betillo", "antoi"}
    print("Index 2")
    print("Hola {}".format(g.nombre))
    grupo = "IDGS-803"
    return render_template("index.html", grupo=grupo, lista=lista)

@app.route('/index')
def index():
    grupo="IDGS803"
    lista = ["Mario", "Pepe", "juan", 24, 25]
    return render_template("index.html",grupo= grupo, lista= lista)

@app.route('/Alumnos', methods=['GET', 'POST'])
def Alumnos():
    alumno_clase = UseForm(request.form)
    mat = nom = edad = correo = ape = ''
    
    if request.method == 'POST' and alumno_clase.validate():
        mat = alumno_clase.matricula.data
        nom = alumno_clase.name.data
        edad = alumno_clase.edad.data
        correo = alumno_clase.email.data
        ape = alumno_clase.apellidos.data

        mensaje= "bienvendio {}".format(nom)
        flash(mensaje)
    return render_template('Alumnos.html', form=alumno_clase, mat=mat, nom=nom, edad=edad, correo=correo, ape=ape)



@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/cine", methods=['GET', 'POST'])

def cine():

    precio_boletos = 12

    boletos_por_persona = 7

    resultado = ""

 

    if request.method == 'POST':

        nombre = request.form.get('nombre')

        cantidad_compradores = request.form.get('cantidadCompradores', 0, type=int)

        boletos = request.form.get('boletos', 0, type=int)

        cineco = request.form.get('cineco', "no")  

 

        if not nombre:

            return render_template('cine.html', resultado="Debes ingresar tu nombre.")

 

        boletos_maximos = cantidad_compradores * boletos_por_persona  

        if boletos > boletos_maximos:

            return f"Exceso de boletos, el máximo es {boletos_maximos}"

 

        if boletos >= 5:

            descuento = 0.15

        elif boletos >= 3:

            descuento = 0.10

        else:

            descuento = 0

 

        total = boletos * precio_boletos

        total_descuento = total * (1 - descuento)

 

        if cineco == "si":

            total_descuento *= 0.90  

 

            total_descuento = round(total_descuento, 2)

 

        resultado = f"{nombre} su total de boletos son: {boletos}, Valor Total a Pagar: ${total_descuento}"

 

    return render_template('cine.html', resultado=resultado)

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
    csrf.init_app(app)
    app.run(debug=True, port=3000)