
class Model_TaxCalculator :
    """
    Pertenece la Capa de Reglas de Negocio (Model)

    Representa los datos para calcular losimpuestos
    """

    def __init__(self, id: int ,
                 labor_income: int,
                 other_income: int,
                 social_security_contribution: int,
                 pension_contribution: int,
                 mortgage_loan_payments: int,
                 donations: int,
                 education_expenses: int,
                 total_taxed_income: int,
                 total_taxable_income: int,
                 total_deductions: int,
                 total_income_taxes: int):
      
         
        """  Representa los datos de de un calculo de impuestos de una persona """
        self.id = id
        self.labor_income = labor_income
        self.other_income = other_income
        self. social_security_contribution = social_security_contribution
        self.pension_contribution = pension_contribution
        self.mortgage_loan_payments = mortgage_loan_payments
        self.donations = donations
        self. education_expenses = education_expenses
        
        self.total_taxed_income= total_taxed_income
        self.total_taxable_income = total_taxable_income
        self.total_deductions = total_deductions
        self.total_income_taxes= total_income_taxes
        
    def EsIgual( self, comparar_con ):
        """ Verifica si esta instancia de la clase es igual a otra """

        assert(self.id == comparar_con.id)
        assert(self.labor_income == comparar_con.labor_income)
        assert(self.other_income == comparar_con.other_income)
        assert(self. social_security_contribution == comparar_con.social_security_contribution)
        assert(self.pension_contribution == comparar_con.pension_contribution)
        assert(self.mortgage_loan_payments == comparar_con.mortgage_loan_payments)
        assert(self.donations == comparar_con.donations)
        assert(self. education_expenses == comparar_con.education_expenses)
        
        assert(self.total_taxed_income == comparar_con.total_taxed_income)
        assert(self.total_taxable_income == comparar_con.total_taxable_income)
        assert(self.total_deductions == comparar_con.total_deductions)
        assert(self.total_income_taxes == comparar_con.total_income_taxes)
             
        return True
        