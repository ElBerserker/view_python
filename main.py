from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin
from suds.client import Client

wsdl="http://www.lynx.server:8080/ServicioEncuestaImplService/ServicioEncuestaImpl?wsdl"
cliente = Client(wsdl)

app=Flask(__name__)

CORS (app)
CORS (app, resources={
    r"/*":{
    "origins":"*"
    }})

# Rutas principales.
@app.route('/')
def inicio():
    return render_template('client_satisfaction_system/index.html')

@app.route('/menu')
def menu():
    return render_template('client_satisfaction_system/MenuAdministrador.html')

@app.route('/gestiondeusuarios')
def usuarios():
    return render_template('client_satisfaction_system/GestionUsuarios.html')

# Rutas de recepcion de informacion.
@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    contrasenia = request.form['contrasenia']
    
    acceso = cliente.service.validarCredenciales(usuario, contrasenia)

    if acceso == 1:
        return redirect('/menu')
    else:
        return redirect('/');
if __name__ == "__main__":
    app.run(debug=True, port="4040", host="www.lynx.pruebas")
