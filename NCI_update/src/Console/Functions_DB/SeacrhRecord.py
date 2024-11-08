def search():    
    import sys
    sys.path.append("src")


    # from Model.TaxCalculatorModel import Model_TaxCalculator
    from Controller.TaxCalculatorController import Controller_TaxCalculator
    from Logic.validations import TaxValidations
    

    try:
        print("\n Selected the option SEARCH. Follow the following steps:")

        # Validación del código de partida
        while True:
            try:
                id = input("Enter the identification number of the record you want to search: ")
                TaxValidations.validation_id(id)

                #Validation of id
           
                searched_calculation = Controller_TaxCalculator.BuscarCodigoID(id)
                break  # Salir del ciclo si no hay errores

            except Exception as err:
                print(f"** Error: Not found a record whit the identification number {id}.")
                raise err

        # Mostrar información de los calculos
        print(" .  .  .  .  .  .  .")
        print(f"* Record found: Total taxed income: {searched_calculation.total_taxed_income}, Total taxable: {searched_calculation.total_taxable_income}, Total deduction: {searched_calculation.total_deductions}, Total taxes tax: {searched_calculation.total_income_taxes}\n")

    except Exception as err:
        print("** Error: Return with other number ID.")
        print(str(err))
