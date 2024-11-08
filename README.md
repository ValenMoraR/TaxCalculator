# Tax Calculator Project

## Version History

- **Version 1**: Developed by Mario Andrade Rojas and Samuel Villa Carmona
- **Version 2**: Developed by Emmanuel Calad Correa and Paula Meneses
- **Version 3**: Developed by Valentina Morales & Steven Oviedo

## Objective 

The objective of this project is to develop a tax calculator that calculates the tax amount payable based on various income and expense parameters. The application will provide users an intuitive interface to input their incomes, payments, donations, among others, and it will show the result for the tax value. 


## How does it work?

The system will ask the person to enter some personal data and after that the person has to enter some information to calculate the tax: 
- Labor incomes
- Other Incomes, 
- Withholding sources
- Social Security Payments
- Pension Contributions
- Mortgage Payments 
- Donations
- Educational Expenses

Then the system will then handle the required calculations and provide the tax value.


## Main Folders:

### sql Folder
This file defines and creates the sql tables, including their relationships, data and types. This project has 3 tables:
- Income declaration 
- Natural Person
- Personal info

### src Folder

##### Console
File responsible for console interaction. It asks the user for their income and expenses and calculates taxes based on the values ​​entered.

#### Controller
This folder manages the database operations, handling tasks such as connecting to the database, executing queries, and processing data.

#### GUI
Core graphical user interface (GUI) file. Allows visual interaction with the user to enter data and display results.

#### TaxCalculator
Contains the main tax calculation logic, with the necessary formulas and rules.

### tests Folder
File containing unit tests (normal cases, extraordinary cases, and error cases) for tax calculations. Verifies the correct functioning of the defined formulas and logic.


## How to Use?
### Ejecución
Para correr el programa por fuera del entorno de desarrollo :
1. Navegar a la carpeta: una vez que hayas clonado el archivo, abre el cmd y navega a la carpeta donde guardaste el archivo, por ejemplo:
   ```bash
   "C:\Users\Usuario\OneDrive\Documentos\U\Sexto Semestre\Código limpio\NCI_update"
   ``` 
2. A continuación puedes ejecutar la consola para comprobar el funcionamiento, esto mediante las siguinetes lineas: <br>
   ```bash

   src\Console\Menu_Console_DB.py
   python src\Console\Menu_Console_DB.py
   ```
   
3. Tambien puedes ejecutar el script principal donde se encuentra la interfaz, la cual es mas amigable con el usuario: <br>
   ```bash
   src\GUI\TaxCalculator_GUI.py
   python src\GUI\TaxCalculator_GUI.py
   ```


This folder contains the implementation of the project's graphical interface. The main file is TaxCalculator_GUI.py, where the visual elements that allow the user to interact with the calculator in a more intuitive and user-friendly way are located.

This file uses Kivy's graphical libraries to create the window, buttons, and input fields needed to enter the user's data (income and expenses), and displays the result of the calculation on the screen. 

### Data Base 
The database was created with (https://neon.tech/), in this we created 1 tables:
- taxcalculator

#### Use of the Data Base
Install the necessary library to connect the SQL database, by running in the terminal

    pip install psycopg2 

Then fill in this information and save this file as Secret_Config.py
to be able to run the application.

    PGDATABASE = "ENTER THE NAME OF THE DATABASE"
    PGUSER = "ENTER THE DATABASE USER"
    PGPASSWORD = "ENTER THE PASSWORD"
    PGHOST = "ENTER THE DNS ADDRESS OR IP ADDRESS OF THE SERVER"
    PGPORT = 5432 

###### DEFAULT IS 5432, BUT IT MAY CHANGE IN YOUR DB

By following these steps you should now have your database correctly connected to your project.

To create and configure the secret_config, first you have to move them to a new file called "secret_config.py" so that we can call it this way in our controller, which is where we performed our previous database connection process.

Then you have to add it to the '''.gitignore''' file, with that, our credentials are completely secure and we are not at risk of data leakage.
