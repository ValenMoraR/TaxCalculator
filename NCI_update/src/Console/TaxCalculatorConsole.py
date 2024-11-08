import sys
sys.path.append('src')
from Logic.logic import IncomeTaxes
from Model.TaxCalculatorModel import Model_TaxCalculator
from Controller.TaxCalculatorController import Controller_TaxCalculator


def validate_empty(value):
    return int(value) if value else 0  # Convertimos el valor a entero, o 0 si está vacío

print("<<< PROGRAM RUNNING >>>")
print("::::::::::::::::::::::::::::::::")
print("**NOTE: For data that does not apply to your profile, please leave it blank, just press ENTER and continue with the next data point")
print("Remember that all the data you enter is calculated as annual percentages and in Colombian pesos.")
print("----------------------------------------------------------------------")
id = validate_empty(input("Enter your identification number: "))
labor_income = validate_empty(input("Enter your annual employment income ($COP): "))
other_income = validate_empty(input("Enter the sum of your other income: "))
social_security_contribution = validate_empty(input("Enter your contribution to social security: "))
pension_contribution = validate_empty(input("Enter your contribution to pension: "))
mortgage_loan_payments = validate_empty(input("Enter your mortgage loan payments: "))
donations = validate_empty(input("Enter your donations: "))
education_expenses = validate_empty(input("Enter your education expenses: "))


try:
    # Crea la instancia con la función que realiza la validación
    taxes = IncomeTaxes.validate_variables(id=id,labor_income=labor_income, other_income=other_income, social_security_contribution=social_security_contribution,
                                pension_contribution=pension_contribution, mortgage_loan_payments=mortgage_loan_payments, donations=donations, education_expenses=education_expenses)
    
  
    summary = taxes.get_calculation()
    print("-  -  -  -  -  -  -  -  -  -  -  -  -")
    print("Calculate tax!\n")
    print(f'ID: {summary["id"]}')
    print(f'Labor income: {summary["labor_income"]}')
    print(f'Other income: {summary["other_income"]}')
    print(f'Social security: {summary["social_security_contribution"]}')
    print(f'Pension contribution: {summary["pension_contribution"]}')
    print(f'Mortgage loan payments: {summary["mortgage_loan_payments"]}')
    print(f'Donations: {summary["donations"]}')
    print(f'Education expenses: {summary["education_expenses"]}')
    print(f"The total amount of taxed income is: {summary['total_taxed_income']:.2f}") #Ingresos gravados -> saladio
    print(f"The total amount of untaxed income is: {summary['total_taxable_income']:.2f}") #Ingresos no gravados -> otros ingresos con iva
    print(f"The total amount of deductions is: {summary['total_deductions']:.2f}") #Deducibles 
    print(f"The total amount of taxes to be paid is: {summary['total_income_taxes']:.2f}") #Impuestos de renta
    
    
    # Crear instancia para almacenar en la base de datos
    calculation = Model_TaxCalculator(
        id=summary['id'],
        labor_income=int(summary['labor_income']),
        other_income=int(summary['other_income']),
        social_security_contribution=int(summary['social_security_contribution']),
        pension_contribution=int(summary['pension_contribution']),
        mortgage_loan_payments=int(summary['mortgage_loan_payments']),
        donations=int(summary['donations']),
        education_expenses=int(summary['education_expenses']),
        total_taxed_income= int(summary['total_taxed_income' ]),                       
        total_taxable_income=int(summary['total_taxable_income']),
        total_deductions=int(summary['total_deductions']),
        total_income_taxes=int(summary['total_income_taxes'])
    )

    # Guardar en la base de datos
    Controller_TaxCalculator.Insertar(calculation)
    print("-  -  -  -  -  -  -  -  -  -  -  -  -\n")
    print("Data of starting uploaded in the database correctly!")

    # Realizar cálculo de impuestos
    result = taxes.calculate_total_taxes()
    print(f"The total amount of taxes to be paid is: {result}")
    
except Exception as up_error:   
    print("*** ERROR ***")
    print(str(up_error))
