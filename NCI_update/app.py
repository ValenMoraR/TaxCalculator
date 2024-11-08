import sys
import psycopg2
sys.path.append('src')
from Controller.TaxCalculatorController import Controller_TaxCalculator

# Para las aplicaciones web creadas con Flask, debemos importar siempre el modulo 
from flask import Flask    

# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
from flask import render_template, request , redirect, url_for, flash

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     

@app.route('/')
def index():
    try:
        return render_template("buscar_registro_id.html")
    except psycopg2.Error as e:
        flash(f"**Error: El ID ingresado no es válido {e}")
        return redirect(url_for('buscar_registro_id'))

@app.route('/buscar_registro_id')
def buscar_registro():
   
    id = request.args["id"]
    def validar_numero(valor):
        """Función que verifica si el valor es un número."""
        if not valor.isdigit():
            return render_template("buscar_registro_id.html")
    validar_numero(id)
    searched_calculation = Controller_TaxCalculator.BuscarCodigoID(id)
    return render_template("datos_taxcalculator.html", registro_buscado=searched_calculation)
    
#    return render_template("datos_taxcalculator.html")


# # decorator: se usa para indicar el URL Path por el que se va a invocar nuestra función
# @app.route('/')      
# def hello():
#     return 'Hola <i>Clase de Codigo Limpio</i> Cruel!'
  
# # para retornar plantillas HTML almacenadas en la carpeta templates, se usa a render_template  
# @app.route('/hola')      
# def html():
#     return render_template('hola.html')

# @app.route('/compra')      
# def compra():
#     return render_template('compra.html')

# @app.route('/calcular_cuota')
# def calcular_cuota():
#     compra = request.args["compra"]
#     return "La compra fue de : " + compra

# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__=='__main__':
   app.run( debug=True)