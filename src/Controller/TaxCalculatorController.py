import sys
sys.path.append( "." )
sys.path.append( "src" )

import psycopg2

from Model.TaxCalculatorModel import Model_TaxCalculator
import SecretConfig

class Controller_TaxCalculator:

    def BorrarTodo():
        """ Borra todos las filas de la tabla taxcalculator"""
        cursor = Controller_TaxCalculator.ObtenerCursor()
        cursor.execute(  "delete from taxcalculator;")
        cursor.connection.commit()

    def CrearTabla():
        """ Crea la tabla de taxcalculator en la BD """
        cursor = Controller_TaxCalculator.ObtenerCursor()

        cursor.execute("""create table taxcalculator (id int primary key not null,
        labor_income int not null,
        other_income int not null,
        social_security_contribution int not null ,
        pension_contribution int not null,
        mortgage_loan_payments int not null,
        donations int not null,
        education_expenses int not null,
        total_taxed_income int,
        total_taxable_income int,
        total_deductions int,
        total_income_taxes int
        ); """)
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla taxcalculator de la BD """
        cursor = Controller_TaxCalculator.ObtenerCursor()

        cursor.execute("""drop table if exists taxcalculator""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()


    def Insertar( calculation : Model_TaxCalculator) :
        """ Recibe un a instancia de la clase Model_TaxCalculator y la inserta en la tabla respectiva"""
        cursor = Controller_TaxCalculator.ObtenerCursor()
        cursor.execute( f"""insert into taxcalculator (id, labor_income, other_income, social_security_contribution, pension_contribution,
                        mortgage_loan_payments, donations, education_expenses,total_taxed_income, total_taxable_income, total_deductions, total_income_taxes) 
                        values ({calculation.id}, {calculation.labor_income}, {calculation.other_income}, {calculation.social_security_contribution}, 
                        {calculation.pension_contribution}, {calculation.mortgage_loan_payments}, {calculation.donations}, {calculation.education_expenses}, 
                        {calculation.total_taxed_income},{calculation.total_taxable_income}, {calculation.total_deductions}, {calculation.total_income_taxes})""" )

        cursor.connection.commit()

    def EliminarRegistro(id):
        """ Elimina un registro de calculo de impuestos de la tabla taxcalculate dado el id de la persona """
        cursor = Controller_TaxCalculator.ObtenerCursor()
        
        # Verificar si el registro existe
        cursor.execute(f"""select id, labor_income, other_income, social_security_contribution, pension_contribution,
                        mortgage_loan_payments, donations, education_expenses, total_taxed_income, total_taxable_income, total_deductions, total_income_taxes
                       from taxcalculator where id = {id}""")
        fila = cursor.fetchone()

        Controller_TaxCalculator.ValidarExistenciaDeRegistro(fila,id )

        # Ejecutar la consulta DELETE
        cursor.execute(f"DELETE FROM taxcalculator WHERE id = {id}")
        
        # Confirmar los cambios
        cursor.connection.commit()

    def BuscarCodigoID( id ) -> Model_TaxCalculator:
        """ Trae los datos del juego dado su codigo de partida """
        cursor = Controller_TaxCalculator.ObtenerCursor()

        cursor.execute(f"""select id, labor_income, other_income, social_security_contribution, pension_contribution,
                        mortgage_loan_payments, donations, education_expenses, total_taxed_income, total_taxable_income, total_deductions, total_income_taxes
        from taxcalculator where id = {id}""" )
        fila = cursor.fetchone()

        Controller_TaxCalculator.ValidarExistenciaDeRegistro(fila,id )
        
        resultado = Model_TaxCalculator( id=fila[0], labor_income=fila[1], other_income=fila[2], social_security_contribution=fila[3], 
                                        pension_contribution=fila[4], mortgage_loan_payments=fila[5], donations=fila[6], education_expenses=fila[7],
                                        total_taxed_income=fila[8], total_taxable_income=fila[9], total_deductions=fila[10], total_income_taxes=fila[11])
               
        return resultado
    
    def Actualizar(id, updated_calculation: Model_TaxCalculator):
        """ Actualiza los datos de un calculo de impuestos en la base de datos dado id de la persona """
        cursor = Controller_TaxCalculator.ObtenerCursor()

        Controller_TaxCalculator.ValidarRegistroDeAcualizacion(id )

        # Ejecutar la actualización de los datos del nuevo calculo de impuesto proporcionados
        cursor.execute(f"""
            UPDATE taxcalculator
            SET labor_income = {updated_calculation.labor_income},
                other_income = {updated_calculation.other_income},
                social_security_contribution = {updated_calculation.social_security_contribution},
                pension_contribution = {updated_calculation.pension_contribution},
                mortgage_loan_payments = {updated_calculation.mortgage_loan_payments},
                donations = {updated_calculation.donations},
                education_expenses = {updated_calculation.education_expenses},
                total_taxed_income = {updated_calculation.total_taxed_income},
                total_taxable_income = {updated_calculation.total_taxable_income},
                total_deductions = {updated_calculation.total_deductions},
                total_income_taxes = {updated_calculation.total_income_taxes}
            WHERE id = '{id}';
        """)

        # Confirmar los cambios
        cursor.connection.commit()

    def ValidarExistenciaDeRegistro(fila,id):
        if not fila:
            raise Exception(f"No se encontró registro con el siguiente ID: {id}")  

    def ValidarRegistroDeAcualizacion (id):  
        try:
            Controller_TaxCalculator.BuscarCodigoID(id)  # Intentar buscar el registro
        except Exception as e:
            raise Exception(f"No se encontró registro con el siguiente ID: {id}") from e

    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor