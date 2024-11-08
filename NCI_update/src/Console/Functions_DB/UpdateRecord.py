def update():
    import sys
    sys.path.append("src")

    from Model.TaxCalculatorModel import Model_TaxCalculator
    from Controller.TaxCalculatorController import Controller_TaxCalculator
    from Logic import exceptions
    from Logic.validations import TaxValidations

    try:
        updated_calculation = Model_TaxCalculator(id=0, labor_income=0, other_income=0, social_security_contribution=0,
                    pension_contribution=0,mortgage_loan_payments=0, donations=0, education_expenses=0, total_taxed_income=0, total_taxable_income= 0, total_deductions=0, total_income_taxes=0)
        
        print("\nSelected the option UPDATE. Follow the following steps:")

        # Validación del código de partida existente
        while True:
            try:
                id = input("Enter the identification number of the record you want to update: ")
                TaxValidations.validation_id(id)

                searched_calculation = Controller_TaxCalculator.BuscarCodigoID(id)
                print(f"* Record found with identification {id}: Total taxed income: {searched_calculation.total_taxed_income}, Total taxable: {searched_calculation.total_taxable_income}, Total deduction: {searched_calculation.total_deductions}, Total taxes tax: {searched_calculation.total_income_taxes}")
                break
            #Validation data
            except Exception as error:
                print(f"**Error:  Not found a record whit the identification number {id}.")
                raise error

        print(" .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .")
        print(f" * * * Enter new data to update the record with identification: {id}")

        # Validación de filas y columnas
        while True:
            try:
                updated_calculation.labor_income= input("Enter your annual employment income ($COP): ")
                TaxValidations.validate_and_convert(updated_calculation.labor_income, "labor_income")
                
                updated_calculation.other_income= input("Enter the sum of your other income: ")
                TaxValidations.validate_and_convert(updated_calculation.other_income, "other_income")
                
                updated_calculation.social_security_contribution= input("Enter your contribution to social security: ")
                TaxValidations.validate_and_convert(updated_calculation.social_security_contribution, "social_security_contribution")
                
                updated_calculation.pension_contribution = input("Enter your contrubution to pension: ")
                TaxValidations.validate_and_convert(updated_calculation.pension_contribution, "pension_contribution")
                
                updated_calculation.mortgage_loan_payments = input("Enter your mortgage loan payments: ")
                TaxValidations.validate_and_convert(updated_calculation.mortgage_loan_payments, "mortgage_loan_payments")
                
                updated_calculation.donations = input("Enter your donations: ")
                TaxValidations.validate_and_convert(updated_calculation.donations, "donations")
                
                updated_calculation.education_expenses = input("Enter your education expenses: ")
                TaxValidations.validate_and_convert(updated_calculation.education_expenses, "education_expenses")
                
                updated_calculation.total_taxed_income = input("Enter the new total taxed: ")
                TaxValidations.validate_and_convert(updated_calculation.total_taxed_income, "total_taxed_income")
                
                updated_calculation.total_taxable_income = input("Enter the new total taxable: ")
                TaxValidations.validate_and_convert(updated_calculation.total_taxable_income,"total_taxable_income" )
                
                updated_calculation.total_deductions = input("Enter the new total deductions: ")
                TaxValidations.validate_and_convert(updated_calculation.total_deductions,"total_deductions")
                
                updated_calculation.total_income_taxes = input("Enter the new total tax pay: ")
                TaxValidations.validate_and_convert(updated_calculation.total_income_taxes, "total_income_taxes")

                updated_calculation.labor_income = int(updated_calculation.labor_income)
                updated_calculation.other_income = int(updated_calculation.other_income)
                updated_calculation.social_security_contribution = int(updated_calculation.social_security_contribution)
                updated_calculation.pension_contribution = int(updated_calculation.pension_contribution)
                updated_calculation.mortgage_loan_payments = int(updated_calculation.mortgage_loan_payments)
                updated_calculation.donations = int(updated_calculation.donations)
                updated_calculation.education_expenses = int(updated_calculation.education_expenses)
                
                updated_calculation.total_taxed_income = int(updated_calculation.total_taxed_income)
                updated_calculation.total_taxable_income = int(updated_calculation.total_taxable_income)
                updated_calculation.total_deductions = int(updated_calculation.total_deductions)
                updated_calculation.total_income_taxes = int(updated_calculation.total_income_taxes)
                break

            except Exception as err:
                print("** Error: Make sure you enter the data correctly.")
                print(str(err))
                
        # Actualizar la partida
        update_calculate = Controller_TaxCalculator.Actualizar(id, updated_calculation)
        
        # Verificar la actualización
        update_records_tax = Controller_TaxCalculator.BuscarCodigoID(id)
        print(" .  .  .  .  .  .  .")
        print(f"* Records indentify {id} updated succesfully: Total taxed income: {update_records_tax.total_taxed_income},Total taxable income: {update_records_tax.total_taxable_income}, Total deductions: {update_records_tax.total_deductions}, Total income taxes: {update_records_tax.total_income_taxes}\n")

    except Exception as err:
        print("** Error: Asegúrese de que la partida exista.")
        print(str(err))