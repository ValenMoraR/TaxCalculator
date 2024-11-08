import sys
sys.path.append('src')
from Logic.validations import TaxValidations

class IncomeTaxes():
    def __init__(self, id, labor_income, other_income=0, social_security_contribution=0,
                 pension_contribution=0,mortgage_loan_payments=0, donations=0, education_expenses=0):
        
        self.id = id
        self.labor_income= labor_income
        self.other_income= other_income
        self.social_security_contribution= social_security_contribution
        self.pension_contribution = pension_contribution
        self.mortgage_loan_payments = mortgage_loan_payments
        self.donations = donations
        self.education_expenses = education_expenses

        self.variable = {
            'total_taxed_income': 0, #ingresos gravados - 
            'total_taxable_income' : 0, #ingresos no gravados
            'total_deductions' : 0,
            'total_income_taxes' : 0            
        }
        
         # Constantes de deducción
        self.IVA= 0.19
        self.PORCENTAGE_TO_DEDUCTION_SSC = 0.1  # Deducción de aporte a seguridad social
        self.PORCENTAGE_TO_DEDUCTION_PC = 0.06  # Deducción de aporte a pensión
        self.PORCENTAGE_TO_DEDUCTION_MLO = 0.22  # Deducción de créditos hipotecarios
        self.PORCENTAGE_TO_DEDUCTION_D = 0.05  # Deducción de donaciones
        self.PORCENTAGE_TO_DEDUCTION_EE = 0.2  # Deducción de gastos en educación
        self.PORCENTAGE_TO_DEDUCTION_WS = 0.04 # Retencion de fuente 
        
        self.get_calculation()
    
    def validate_variables(id, labor_income, other_income=0, social_security_contribution=0,
                        pension_contribution=0, mortgage_loan_payments=0, donations=0, education_expenses=0):
    
        # Realiza todas las validaciones aquí antes de crear la instancia
        id= TaxValidations.validate_and_convert(id, 'id')
        labor_income = TaxValidations.validate_and_convert(labor_income, 'labor_income')
        other_income = TaxValidations.validate_and_convert(other_income, 'other_income')
        social_security_contribution = TaxValidations.validate_and_convert(social_security_contribution, 'social_security_contribution')
        pension_contribution = TaxValidations.validate_and_convert(pension_contribution, 'pension_contribution')
        mortgage_loan_payments = TaxValidations.validate_and_convert(mortgage_loan_payments, 'mortgage_loan_payments')
        donations = TaxValidations.validate_and_convert(donations, 'donations')
        education_expenses = TaxValidations.validate_and_convert(education_expenses, 'education_expenses')
        
        # Crear y retornar la instancia
        return IncomeTaxes(id, labor_income, other_income, social_security_contribution,
                        pension_contribution, mortgage_loan_payments, donations, education_expenses)
        
    '''Calculate the total of other income plus IVA'''
    def calculate_taxed_income(self):
        taxed_income= self.other_income * self.IVA
        taxed_income = self.other_income + taxed_income 
        self.variable['total_taxed_income'] = taxed_income
        return taxed_income

    """Calculate total income by adding employment income and other income."""
    def calculate_total_income(self):
        sum_other_income= self.calculate_taxed_income()
        return self.labor_income + sum_other_income
        
    """Calculate the total deductions based on the allowed percentages."""
    def calculate_deductions(self):
        deduction_ssc = self.social_security_contribution * self.PORCENTAGE_TO_DEDUCTION_SSC
        deduction_pc = self.pension_contribution * self.PORCENTAGE_TO_DEDUCTION_PC
        deduction_mlo = self.mortgage_loan_payments * self.PORCENTAGE_TO_DEDUCTION_MLO
        deduction_d = self.donations * self.PORCENTAGE_TO_DEDUCTION_D
        deduction_ee = self.education_expenses * self.PORCENTAGE_TO_DEDUCTION_EE

        # Total de deducciones
        total_deductions = deduction_ssc + deduction_pc + deduction_mlo + deduction_d + deduction_ee
        return total_deductions
    
    #las cosas las cmabio desde aqui
    
    """Calculate taxable income by subtracting deductions from total income."""
    def calculate_taxable_income(self):
        total_income = self.calculate_total_income()
        total_deductions = self.calculate_deductions()
        total_taxable =  total_income - total_deductions
        self.variable['total_taxable_income'] = total_taxable
        return total_taxable
    
    
    """Calculate the withholding tax by applying the withholding percentage."""
    def calculate_withholdings_source(self):
        taxable_income = self.calculate_taxable_income()
        total_deduction_ws = taxable_income * self.PORCENTAGE_TO_DEDUCTION_WS
        self.variable['total_deductions'] = total_deduction_ws
        return total_deduction_ws
    
    """Calculate the total tax payable after applying withholdings at source."""
    def calculate_total_taxes(self):
        if self.labor_income==0:
            raise TaxValidations.validate_labor_income(self.labor_income)
        else:
            withholdings_source = self.calculate_withholdings_source()
            total_pay = withholdings_source - self.PORCENTAGE_TO_DEDUCTION_WS
            self.variable['total_income_taxes'] = total_pay
            return total_pay
        
    '''Esto devuelve el calculo de los valores en un diccionario para mostrarlo al usuario '''
    def get_calculation(self):
            self.calculate_total_income()
            self.calculate_total_taxes()
            return {
            'id': self.id,
            'labor_income':self.labor_income,
            'other_income':self.other_income,
            'social_security_contribution': self.social_security_contribution,
            'pension_contribution': self.pension_contribution,
            'mortgage_loan_payments': self.mortgage_loan_payments,
            'donations': self.donations,
            'education_expenses':self.education_expenses,
            'total_taxed_income':self.variable['total_taxed_income' ],
            'total_taxable_income':self.variable['total_taxable_income'],
            'total_deductions':self.variable['total_deductions'],
            'total_income_taxes' :self.variable['total_income_taxes' ]
        }
        

