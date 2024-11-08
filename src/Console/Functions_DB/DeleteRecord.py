def delete():
    import sys
    sys.path.append("src")

    from Controller.TaxCalculatorController import Controller_TaxCalculator
    from Logic.validations import TaxValidations
    # from Logic import validations
    
    try:
        print("\nSelected the DELETE option. Follow the following steps:")

        # Validación del código de partida
        while True:
            try:
                id = input("Enter the identification number of the record you want to delete: ")
                TaxValidations.validation_id(id)
                
                #Validations of id
                
                # Intentar eliminar el resgistro si el código es válido
                partida_eliminar = Controller_TaxCalculator.EliminarRegistro(id)
                break  # Salir del ciclo si no hay errores

            
            except Exception as err:
                print(f"** Error: Could not delete record with ID: {id}.")
                raise err

        # Mostrar mensaje de éxito
        print(" .  .  .  .  .  .  .")
        print(f"The record with identification number {id} has been deleted succesfully.\n")
    except Exception as err:
        print("** Error: Make sure the item exists in the database.")
        print(str(err))