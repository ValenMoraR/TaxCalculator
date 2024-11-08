import sys
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
sys.path.append('src')
from Controller.TaxCalculatorController import Controller_TaxCalculator
from Model.TaxCalculatorModel import Model_TaxCalculator
from Logic.logic import IncomeTaxes 

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para el uso de mensajes flash

# Ruta del menú principal
@app.route('/')
def index():
    return render_template("index.html")

# Ruta para la búsqueda de un registro
@app.route('/buscar', methods=['GET', 'POST'])
def buscar_registro():
    if request.method == 'POST':
        id = request.form.get("id")

        # Validación del ID
        if not id or not id.isdigit():
            flash("Por favor, ingrese un ID válido (solo números).")
            return redirect(url_for('buscar_registro'))

        try:
            # Realizar la búsqueda en la base de datos
            searched_calculation = Controller_TaxCalculator.BuscarCodigoID(id)

            # Mostrar mensaje si no se encuentra el registro
            if not searched_calculation:
                flash(f"No se encontró ningún registro con ID: {id}.")
                return redirect(url_for('buscar_registro'))

            # Si encuentra el registro, lo muestra
            return render_template("mostrar_registro_buscado.html", registro_buscado=searched_calculation)

        except Exception as e:
            flash(f"Ocurrió un error al buscar el registro: {e}")
            return redirect(url_for('buscar_registro'))
    
    # Si el método es GET, muestra el formulario de búsqueda
    return render_template("buscar_registro_id.html")

@app.route('/insertar', methods=['GET', 'POST'])
def insertar_registro():
    if request.method == 'POST':
        # Validación de cada campo ingresado
        id = request.form.get("id")
        labor_income = request.form.get("labor_income")
        other_income = request.form.get("other_income")
        social_security_contribution = request.form.get("social_security_contribution")
        pension_contribution = request.form.get("pension_contribution")
        mortgage_loan_payments = request.form.get("mortgage_loan_payments")
        donations = request.form.get("donations")
        education_expenses = request.form.get("education_expenses")

        # Diccionario de campos a validar
        campos = {
            "ID": id,
            "Ingresos laborales": labor_income,
            "Otros ingresos": other_income,
            "Contribución a seguridad social": social_security_contribution,
            "Contribución a pensión": pension_contribution,
            "Pagos de préstamo hipotecario": mortgage_loan_payments,
            "Donaciones": donations,
            "Gastos de educación": education_expenses
        }

        # Bandera de validación
        datos_validos = True

        # Validar que cada campo sea un número
        for nombre_campo, valor in campos.items():
            if not valor or not valor.isdigit():
                flash(f"Por favor, ingrese un valor numérico válido para {nombre_campo}.", "error")
                datos_validos = False

        # Si hubo algún error, redirige al formulario sin hacer la inserción
        if not datos_validos:
            return redirect(url_for('insertar_registro'))

        # Crear la instancia de IncomeTaxes con los valores ingresados
        try:
            income_tax = IncomeTaxes(
                id=id,
                labor_income=float(labor_income),
                other_income=float(other_income),
                social_security_contribution=float(social_security_contribution),
                pension_contribution=float(pension_contribution),
                mortgage_loan_payments=float(mortgage_loan_payments),
                donations=float(donations),
                education_expenses=float(education_expenses)
            )

            # Realizar los cálculos
            total_taxed_income = income_tax.calculate_taxed_income()
            total_taxable_income = income_tax.calculate_taxable_income()
            total_deductions = income_tax.calculate_withholdings_source()
            total_income_taxes = income_tax.calculate_total_taxes()

        except Exception as e:
            flash(f"Ocurrió un error en los cálculos de impuestos: {e}", "error")
            return redirect(url_for('insertar_registro'))

        # Crear la instancia del modelo con los datos calculados
        calculation = Model_TaxCalculator(
            id=id,
            labor_income=labor_income,
            other_income=other_income,
            social_security_contribution=social_security_contribution,
            pension_contribution=pension_contribution,
            mortgage_loan_payments=mortgage_loan_payments,
            donations=donations,
            education_expenses=education_expenses,
            total_taxed_income=total_taxed_income,
            total_taxable_income= total_taxable_income,
            total_deductions=total_deductions,
            total_income_taxes= total_income_taxes
        )

        # Insertar en la BD
        try:
            Controller_TaxCalculator.Insertar(calculation)
            # Redirigir a la página de éxito de inserción
            return render_template("insercion_exitosa.html")
        except Exception as e:
            flash(f"Ocurrió un error al insertar en la base de datos: {e}", "error")
            return redirect(url_for('insertar_registro'))

    # Si el método es GET, muestra el formulario de inserción
    return render_template("insertar_registro.html")


@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar_registro():
    if request.method == 'POST':
        id = request.form.get("id")

        # Validación del ID para asegurar que sea un número
        if not id or not id.isdigit():
            flash("Por favor, ingrese un ID válido (solo números).", "error")
            return redirect(url_for('eliminar_registro'))

        try:
            # Intentar eliminar el registro de la base de datos
            Controller_TaxCalculator.EliminarRegistro(id)
            
            # Si no se lanza ninguna excepción, renderiza el template de éxito
            return render_template("eliminacion_exitosa.html", id=id)  # Renderizar el template de éxito

        except ValueError as e:
            # Si se lanza una excepción (por ejemplo, registro no encontrado), muestra el mensaje de error
            flash(str(e), "error")
            return redirect(url_for('eliminar_registro'))
        
        except Exception as e:
            # Para cualquier otro error
            flash(f"Ocurrió un error al intentar eliminar el registro: {e}", "error")
            return redirect(url_for('eliminar_registro'))

    # Si el método es GET, muestra el formulario de eliminación
    return render_template("eliminar_registro.html")



if __name__ == '__main__':
    app.run(debug=True)
