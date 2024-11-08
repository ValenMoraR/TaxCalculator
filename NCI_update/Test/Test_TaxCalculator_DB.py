import unittest
import sys
sys.path.append( "." )

from src.Model.TaxCalculatorModel import Model_TaxCalculator
from src.Controller.TaxCalculatorController import Controller_TaxCalculator

class Test_DB( unittest.TestCase ):

    #Test Fixture
    def setUpClass():
        # Llamar a la clase COntrolador para que cree la tabla
        Controller_TaxCalculator.EliminarTabla()
        Controller_TaxCalculator.CrearTabla()
    
    def test_insert( self ):
        
        # Crear una partida del juego
        calculation = Model_TaxCalculator( id=12345678, labor_income=12000000, other_income=5000000, social_security_contribution=700000,
                                pension_contribution=2500000,mortgage_loan_payments=1000000, donations=500000, education_expenses=300000, 
                                total_taxed_income=100000000,total_taxable_income= 9000000, total_deductions=5000000, total_income_taxes=4000000)
        
        # Guardarla en la BD
        Controller_TaxCalculator.Insertar( calculation )
        
        # Buscarla
        id_search = Controller_TaxCalculator.BuscarCodigoID( id=12345678 )
        
        # Verificar si la trajo bien
        self.assertTrue(  id_search.EsIgual( calculation )  )
    
    def test_insert2( self ):
        
        # Crear una partida del juego
        calculation = Model_TaxCalculator( id=9876546, labor_income=22000000, other_income=4000000, social_security_contribution=900000,
                                pension_contribution=3000000, mortgage_loan_payments=1200000, donations=700000, education_expenses=375000, 
                                total_taxed_income=100000000,total_taxable_income = 13000000, total_deductions=7000000, total_income_taxes=6000000)
        
        # Guardarla en la BD
        Controller_TaxCalculator.Insertar( calculation )
        
        # Buscarla
        id_search = Controller_TaxCalculator.BuscarCodigoID( id=9876546 )
        
        # Verificar si la trajo bien
        self.assertTrue(  id_search.EsIgual( calculation )  )

    
    def test_error_PrimaryKey(self):
        # Inserta una partida en la tabla
        id_prueba  = Model_TaxCalculator( id=88888888, labor_income=16000000, other_income=3000000, social_security_contribution=600000,
                                pension_contribution=5000000, mortgage_loan_payments=2500000, donations=1100000, education_expenses=450000, 
                                total_taxed_income=100000000,total_taxable_income = 12055600, total_deductions=6400000, total_income_taxes=5560348)
        Controller_TaxCalculator.Insertar( id_prueba )

        # Inserta una partida en la tabla
        id_otro  = Model_TaxCalculator( id=88888888, labor_income=20000000, other_income=4000000, social_security_contribution=900000,
                                pension_contribution=2000000, mortgage_loan_payments=1200000, donations=2200000, education_expenses=720000, 
                                total_taxed_income=100000000,total_taxable_income = 21231500, total_deductions=8900000, total_income_taxes=12980555 )
        
        self.assertRaises( Exception, Controller_TaxCalculator.Insertar, id_otro )

    def test_delete( self ):

        #Codigo de partida se desea eliminar
        calculation = Model_TaxCalculator( id=1111111, labor_income=12000000, other_income=2000000, social_security_contribution=450000,
                                pension_contribution=2000000, mortgage_loan_payments=1000000, donations=400000, education_expenses=320000, 
                                total_taxed_income=100000000,total_taxable_income = 9000000, total_deductions=4000000, total_income_taxes=5000000)
        
        Controller_TaxCalculator.Insertar(calculation)
                     
        # Guardarla en la BD
        Controller_TaxCalculator.EliminarRegistro( calculation.id)

    def test_delete_error(self):
        # Código de partida que no existe en la BD
        calculation = Model_TaxCalculator( id=2222222, labor_income=12000000, other_income=2000000, social_security_contribution=450000,
                                pension_contribution=2000000, mortgage_loan_payments=1000000, donations=400000, education_expenses=320000, 
                                total_taxed_income=100000000,total_taxable_income = 9000000, total_deductions=4000000, total_income_taxes=5000000)
        
        # Verificar que lanzar excepción al intentar eliminar un registro inexistente
        self.assertRaises(Exception, Controller_TaxCalculator.EliminarRegistro, calculation.id)

    def test_search_calculation(self):
        # Buscar una partida en la tabla
        busqueda_prueba  = Model_TaxCalculator( id=9999999, labor_income=2200000, other_income=5555555, social_security_contribution=7777770,
                                pension_contribution=2200000,mortgage_loan_payments=1000000, donations=500000, education_expenses=300000, 
                                total_taxed_income=100000000,total_taxable_income = 8795300, total_deductions=5666777, total_income_taxes=4022244 )
        
        Controller_TaxCalculator.Insertar(busqueda_prueba)
        
        busqueda = Controller_TaxCalculator.BuscarCodigoID( busqueda_prueba.id )    

         # Verificar si la trajo bien
        self.assertTrue(  busqueda.EsIgual( busqueda_prueba )  )

    def test_error_search_calculation(self):
        # Buscar una partida en la tabla
        busqueda_prueba  = Model_TaxCalculator( id=2222222, labor_income=12000000, other_income=2000000, social_security_contribution=450000,
                                pension_contribution=2000000, mortgage_loan_payments=1000000, donations=400000, education_expenses=320000, 
                                total_taxed_income=100000000,total_taxable_income = 9000000, total_deductions=4000000, total_income_taxes=5000000 )
                 
        self.assertRaises(Exception, Controller_TaxCalculator.BuscarCodigoID, busqueda_prueba.id)  


    def test_update_calcultion(self):
        #Insertar un registro en la base de datos
        calculation_star = Model_TaxCalculator( id=78787878, labor_income=3300000, other_income=4444432, social_security_contribution=1212121,
                                pension_contribution=1345000,mortgage_loan_payments=1220000, donations=545000, education_expenses=1250000, 
                                total_taxed_income=100000000,total_taxable_income = 6548721, total_deductions=2345322, total_income_taxes=4102304 )
        
        Controller_TaxCalculator.Insertar(calculation_star)

        # Actualizar el registro ingresado anteriormente con nuevos valores
        calculation_update = Model_TaxCalculator(id=78787878, labor_income=8888888, other_income=2222222, social_security_contribution=4747478,
                                pension_contribution=1345000,mortgage_loan_payments=1220000, donations=545000, education_expenses=1250000, 
                                total_taxed_income=100000000,total_taxable_income = 6548721, total_deductions=2345322, total_income_taxes=4102304)
        
        Controller_TaxCalculator.Actualizar(calculation_star.id, calculation_update)

        # Buscar el registro actualizado
        search_calculation = Controller_TaxCalculator.BuscarCodigoID(calculation_star.id)

        # Verificar que los cambios se realizaron correctamente
        self.assertTrue(search_calculation.EsIgual(calculation_update))

    def test_Update_calculation_unknown(self):
        # Intentar actualizar un registro que no existe en la base de datos
        unknown_calculation = Model_TaxCalculator(id=2222222, labor_income=12000000, other_income=2000000, social_security_contribution=450000,
                                pension_contribution=2000000, mortgage_loan_payments=1000000, donations=400000, education_expenses=320000, 
                                total_taxed_income=100000000,total_taxable_income = 9000000, total_deductions=4000000, total_income_taxes=5000000)
        
        self.assertRaises(Exception, Controller_TaxCalculator.Actualizar, unknown_calculation.id, unknown_calculation)    
                  
if __name__ == '__main__':
    unittest.main()        