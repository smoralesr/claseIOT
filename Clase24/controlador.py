from flask import Flask, render_template, request
from modelo import Persona

app = Flask(__name__)


@app.route('/')
def principal():
    return render_template('index.html')


@app.route('/registro')
def inicio():
    return render_template("formulario.html")


@app.route('/procesar', methods=['POST'])
def procesar():

    nombre = request.form.get("nombre")
    edad = request.form.get("edad")
    accion = request.form.get("accion")

    P1 = Persona(nombre, edad)

    if(accion == '1'):
        P1.saludar()

    elif(accion == '2'):
        P1.presentarse()

    elif(accion == '3'):
        P1.despedirse()

    return render_template("mostrar.html", escrito = P1.texto)


if __name__ =="__main__":
    app.run()