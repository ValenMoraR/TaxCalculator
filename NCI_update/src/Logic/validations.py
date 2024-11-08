# src/Logic/validations.py
import sys
sys.path.append('src')
from Logic.exceptions import *

class TaxValidations():
    
    def v_total_income_less_than_deductions(income_taxes):
        total_income = (income_taxes.labor_income + income_taxes.other_income)
        deductions = (income_taxes.social_security_contribution + income_taxes.pension_contribution + income_taxes.mortgage_loan_payments +\
                      income_taxes.mortgage_loan_payments + income_taxes.donations + income_taxes.education_expenses )
        
        if total_income < deductions:
            raise ValueError(f"ERROR: Total income must be worth more than the total deductions.")
    
    def v_labor_income_less_than_zero(income_taxes):
        if income_taxes.labor_income == 0:
            raise   InsufficientLaborIncome(f"ERROR: Employment income cannot be negative and must be greater than zero.")
        
    def v_labor_income_less_than_ssc(income_taxes):
        if income_taxes.social_security_contribution > income_taxes.labor_income:
            raise SocialSecurityPaymentsGreaterThanLaborIncome(f"ERROR: Social Security payments cannot exceed employment income.")
    
    def v_labor_income_less_tahn_pc(income_taxes):
        if income_taxes.pension_contribution > income_taxes.labor_income:
            raise PensionContributionGreaterThanLaborIncome(f"ERROR: Pension contributions cannot exceed employment income.")
    
    def v_labor_income_less_than_mlp(income_taxes):
        if income_taxes.mortgage_loan_payments > income_taxes.labor_income:
            raise MortgageLosnPaymentsGreaterThanLaborIncome(f"ERROR: Mortgage loan payments cannot exceed employment income.")
    
    def v_labor_income_less_than_donations(income_taxes):
        if income_taxes.donations  > income_taxes.labor_income:
            raise DonationsGreaterThanLaborIncome(f"ERROR: Donations cannot exceed employment income.")
    
    def v_labor_income_less_than_ee(income_taxes):
        if income_taxes.education_expenses > income_taxes.labor_income: 
            raise EducationExpensesGreaterthanLaborIncome(f"ERROR: Education expenses cannot exceed employment income.")
    
    def v_total_income_less_than_ee(income_taxes):
        total_income = (income_taxes.labor_income + income_taxes.other_income)
        if income_taxes.education_expenses > total_income:
            raise EducationExpensesGreaterThanTotalIncome(f"ERROR: Education expenses cannot exceed the sum of total income.")
    
    def v_labor_income_less_than_deductions(income_taxes):
        deductions =(income_taxes.social_security_contribution + income_taxes.pension_contribution + income_taxes.mortgage_loan_payments +\
        income_taxes.mortgage_loan_payments + income_taxes.donations + income_taxes.education_expenses )
        
        if income_taxes.labor_income < deductions :
            raise InsufficientLaborIncome(f"ERROR: Employment income is not sufficient to cover deductions.")
    
    def validation_id(id):
        if not (id).isdigit():
            raise NonNumericValueError("ERROR: The value entered is not numerical.")
    
    def validate_labor_income(labor_income): 
        if labor_income == 0: 
            raise InsufficientLaborIncome("ERROR: Employment income cannot be zero.")
        
    
    def validate_empty(value):
        return int(value) if value else 0  # Convertimos el valor a entero, o 0 si está vacío
        
    def validate_and_convert(entry, variable_name, should_be_integer=False):
        try:
            entry_str = str(entry)
            
            # Check if the entry contains a comma as a decimal separator
            if ',' in entry_str:
                raise CommaSeparator(f"ERROR: Invalid data in {variable_name}\n Use a period (.) as a decimal separator, not a comma (,).")

            # Convert to float to ensure it's numeric
            value = float(entry)

            # If it should be an integer, check that it has no decimals
            if should_be_integer and value != int(value):
                raise NotAnIntegerValue(f"ERROR: Invalid data in {variable_name}\n An integer value was expected.")

            # Check if it's negative
            if value < 0:
                raise NegativeValue(f"ERROR: Invalid data in {variable_name}\n Numbers cannot be negative.")

            # Return the correct type (integer or float)
            return int(value) if should_be_integer else value

        except ValueError:
            raise InvalidValue(f"ERROR: Invalid data in {variable_name}: Ensure it is a numeric value.\n not negative and without letters or special characters.")

