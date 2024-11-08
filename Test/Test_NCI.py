import unittest
import sys
sys.path.append("src")
from Logic import logic
from Logic.logic import IncomeTaxes
from Logic.validations import TaxValidations
from Logic.exceptions import *


class NewTaxresultTest(unittest.TestCase):
    
     #normal test (expeted cases)=================================================================================================
    def test_NormalCasel1(self):
        result = logic.IncomeTaxes(id=12345678,labor_income=96000000,other_income=200000)
        self.assertEqual(result.calculate_total_income(),96238000.0)
    
    def test_NormalCase2(self):
        calculator = logic.IncomeTaxes(id=1234567,labor_income = 14000000,other_income = 2000000,
                                        social_security_contribution = 800000,pension_contribution = 500000,
                                        mortgage_loan_payments = 300000,donations = 150000,education_expenses = 200000)
        expected_value = 646259.96
        result = calculator.calculate_total_taxes()
        self.assertEqual(result, expected_value)
    
    def test_NormalCase3(self):    
        result = logic.IncomeTaxes( id=123456,labor_income = 14000000, other_income = 2000000, 
                                    social_security_contribution = 800000, pension_contribution = 500000) 
        expected_value = 650800.0
        result = result.calculate_withholdings_source() 
        self.assertEqual(result, expected_value)
        
    def test_NormalCase4(self): 
        result = logic.IncomeTaxes( id=12345,labor_income = 14000000, other_income = 2000000, 
                                       mortgage_loan_payments = 300000, donations = 150000, 
                                       education_expenses = 200000) 
        expected_value= 113500.0
        result= result.calculate_deductions() 
        self.assertEqual(result, expected_value)
        
    def test_NormalCase5(self):
        calculator = logic.IncomeTaxes(id=1234,labor_income = 491060000,other_income = 2000000,
                                        social_security_contribution = 8000,pension_contribution = 5000000,
                                        mortgage_loan_payments=3000000, donations=1500000, education_expenses=200000)
        expected_value= 19694568.0
        result = calculator.calculate_withholdings_source()
        self.assertEqual(result, expected_value)
    
    def test_NormalCase6(self):
        calculator = logic.IncomeTaxes(id=123,labor_income = 55700600,social_security_contribution = 800,pension_contribution = 500000,)
        expected_value = 55670520.0
        result = calculator.calculate_taxable_income()
        self.assertEqual(result, expected_value)
    
    
    # Extraordinary tests (boundary or unusual cases)===============================================================================================0
    def test_ExtraordinaryCase1(self):
        result = logic.IncomeTaxes(id=87654321,labor_income=96000000,other_income=-200000)
        self.assertEqual(result.calculate_total_income(),95762000.0)
    
    def test_ExtraordinaryCase2(self):
        calculator = logic.IncomeTaxes(id=7654321,labor_income = 14000000,other_income = 2000000,
                                        social_security_contribution = 800000,pension_contribution = -500000,
                                        mortgage_loan_payments = -123456,donations = 150000,education_expenses = 200000)
        expected_value = 652386.3728
        result = calculator.calculate_total_taxes()
        self.assertEqual(result, expected_value)
    
    def test_ExtraordinaryCase3(self):    
        result = logic.IncomeTaxes( id=654321,labor_income = 14000000, other_income = 200, 
                                    social_security_contribution = 80, pension_contribution = -500000) 
        expected_value = 561209.2000000001
        result = result.calculate_withholdings_source() 
        self.assertEqual(result, expected_value)
        
    def test_ExtraordinaryCase4(self): 
        result = logic.IncomeTaxes(id=54321, labor_income = 1400000, other_income = 2000, 
                                       mortgage_loan_payments = -300, donations = 15000) 
        expected_value= 684.0
        result= result.calculate_deductions() 
        self.assertEqual(result, expected_value)
        
    def test_ExtraordinaryCase5(self):
        calculator = logic.IncomeTaxes(id=4321,labor_income = 491060000,other_income = 2000000,
                                        social_security_contribution = -800000,pension_contribution = 5000000,
                                         education_expenses=-200000)
        expected_value= 19730400.0
        result = calculator.calculate_withholdings_source()
        self.assertEqual(result, expected_value)
    
    def test_ExtraordinaryCase6(self):
        calculator = logic.IncomeTaxes(id=321,labor_income = 55700600,pension_contribution = -500000)
        expected_value = 55730600.0
        result = calculator.calculate_taxable_income()
        self.assertEqual(result, expected_value)
        
    # Error tests (error handling)===============================================================================================================
    # 1. Test para valores de ingreso laboral insuficientes
    def test_insufficient_labor_income(self):
        income_taxes = IncomeTaxes(
            id=1234,
            labor_income=10000, 
            other_income=0, 
            social_security_contribution=5000, 
            pension_contribution=3000, 
            mortgage_loan_payments=2000,
            donations=500, 
            education_expenses=1500)
        with self.assertRaises(InsufficientLaborIncome):
            TaxValidations.v_labor_income_less_than_deductions(income_taxes)  # ingreso laboral insuficiente para el caso
    
    # 2. Test para valores negativos en el ingreso laboral
    def test_negative_labor_income(self):
        with self.assertRaises(NegativeValue):
            IncomeTaxes.validate_variables(id=8492984,labor_income=-50000,other_income=0,social_security_contribution=0,
                                            pension_contribution=0,mortgage_loan_payments=0,donations=0,education_expenses=0)
            
    def test_zero_labor_income(self):
        income_taxes = IncomeTaxes(
            id=52823974,
            labor_income=0)
        with self.assertRaises(InsufficientLaborIncome):
            TaxValidations.v_labor_income_less_than_zero(income_taxes)

    # 3. Test para caracteres no numéricos en ingresos laborales
    def test_invalid_labor_income_value(self):
        with self.assertRaises(InvalidValue):
            IncomeTaxes.validate_variables(id=2674995,labor_income= "invalid")

    # 4. Tesr para gastos de seguridad social mayores a los ingresos laborales
    def test_social_security_greater_than_labor_income(self):
        income_taxes = IncomeTaxes(
            id= 97356759,
            labor_income=100000, 
            other_income=0, 
            social_security_contribution=120000, 
            pension_contribution=3000, 
            mortgage_loan_payments=2000,
            donations=500, 
            education_expenses=1500
        )
        with self.assertRaises(SocialSecurityPaymentsGreaterThanLaborIncome):
            TaxValidations.v_labor_income_less_than_ssc(income_taxes)

    # 5. Test para aportes de pension mayores a los ingresos laborales
    def test_pension_contribution_greater_than_labor_income(self):
        income_taxes = IncomeTaxes(
            id= 45673,
            labor_income=80000, 
            other_income=0, 
            social_security_contribution=5000, 
            pension_contribution=90000, 
            mortgage_loan_payments=2000,
            donations=500, 
            education_expenses=1500
        )
        with self.assertRaises(PensionContributionGreaterThanLaborIncome):
            TaxValidations.v_labor_income_less_tahn_pc(income_taxes)
            
    # 6. Test para pagos de creditos mayores a los ingresos laborales
    def test_mortgage_payments_greater_than_labor_income(self):
        income_taxes = IncomeTaxes(
            id= 9192939,
            labor_income=70000, 
            other_income=0, 
            social_security_contribution=5000, 
            pension_contribution=3000, 
            mortgage_loan_payments=80000,
            donations=500, 
            education_expenses=1500
        )
        with self.assertRaises(MortgageLosnPaymentsGreaterThanLaborIncome):
            TaxValidations.v_labor_income_less_than_mlp(income_taxes)

    # 7. Test para gastos en educación mayores que los ingresos laborales
    def test_education_expenses_greater_than_labor_income(self):
        income_taxes = IncomeTaxes(
            id= 102938,
            labor_income=50000, 
            other_income=0, 
            social_security_contribution=5000, 
            pension_contribution=3000, 
            mortgage_loan_payments=2000,
            donations=500, 
            education_expenses=60000
        )
        with self.assertRaises(EducationExpensesGreaterthanLaborIncome):
            TaxValidations.v_labor_income_less_than_ee(income_taxes)
    
    
if __name__ == "__main__":
     unittest.main()
        
    
    
