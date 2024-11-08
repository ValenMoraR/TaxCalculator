from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
import sys
sys.path.append("src")
from Logic.logic import IncomeTaxes
from Logic.validations import TaxValidations
from Logic.exceptions import *



class TaxesCalculatorApp(App):
    def build(self):
        contenedor = BoxLayout(orientation='vertical')

        # Fondo celeste pastel
        contenedor.canvas.before.clear()
        with contenedor.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(0.8, 0.6, 1, 1)
            self.rect = Rectangle(size=contenedor.size, pos=contenedor.pos)
        contenedor.bind(size=self._update_rect, pos=self._update_rect)

        # Título e instrucciones
        contenedor.add_widget(Label(text="Taxes Calculator", color = (0.3, 0, 0.3, 1), font_size='18sp',bold=True))
        contenedor.add_widget(Label(text="NOTE: For data that does not apply to your profile, please leave it blank, just press ENTER and continue with the next data point", color=(0, 0, 0, 1), font_size='13sp',bold=True))
        contenedor.add_widget(Label(text="Remember that all the data you enter is calculated as annual percentages and in Colombian pesos", color=(0, 0, 0, 1), font_size='13sp',bold=True))

        # Crear campos de entrada con etiquetas
        self.inputs = {}
        fields = [
            ("Labor income:", "labor_income"),
            ("Other income:", "other_income"),
            ("Social security contribution:", "social_security_contribution"),
            ("Pension contribution:", "pension_contribution"),
            ("Mortgage loan payments:", "mortgage_loan_payments"),
            ("Donations:", "donations"),
            ("Education expenses:", "education_expenses")
        ]

        for label_text, field_name in fields:
            label = Label(text=label_text, color=(0, 0, 0, 1))
            text_input = TextInput(multiline=False)
            self.inputs[field_name] = text_input
            contenedor.add_widget(label)
            contenedor.add_widget(text_input)

        # Crear etiquetas para mostrar los resultados
        self.taxed_income_label = Label(text="The total amount of taxed income is: $0", color=(0, 0, 0, 1), bold=True)
        self.taxable_income_label = Label(text="The total amount of untaxed income is: $0", color=(0, 0, 0, 1),bold=True)
        self.deductions_label = Label(text="The total amount of deductions is: $0", color=(0, 0, 0, 1),bold=True)
        self.income_taxes_label = Label(text="The total amount of taxes to be paid is: $0", color=(0, 0, 0, 1),bold=True)

        # Añadir etiquetas de resultados al layout
        contenedor.add_widget(self.taxed_income_label)
        contenedor.add_widget(self.taxable_income_label)
        contenedor.add_widget(self.deductions_label)
        contenedor.add_widget(self.income_taxes_label)
 
        # Botón de cálculo
        button_container = BoxLayout(orientation='horizontal', size_hint=(1, None), height=100)
        calculate_button = Button(text='Calculate', size_hint=(None, None), size=(170, 80),
                                  background_color=(0.3, 0, 0.3, 1), color=(1, 1, 1, 1), bold=True)
        calculate_button.bind(on_press=self.calculate)
        button_container.add_widget(calculate_button)
        contenedor.add_widget(button_container)
   
        return contenedor

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def calculate(self, instance):
        try:
            # Obtener y validar las entradas del usuario
            labor_income = self.inputs["labor_income"].text or "0"
            other_income = self.inputs["other_income"].text or "0"
            social_security_contribution = self.inputs["social_security_contribution"].text or "0"
            pension_contribution = self.inputs["pension_contribution"].text or "0"
            mortgage_loan_payments = self.inputs["mortgage_loan_payments"].text or "0"
            donations = self.inputs["donations"].text or "0"
            education_expenses = self.inputs["education_expenses"].text or "0"

            # Validación y cálculo
            taxes = IncomeTaxes.validate_variables(
                labor_income, other_income, social_security_contribution,
                pension_contribution, mortgage_loan_payments, donations, education_expenses
            )

            # Realizar cálculos individuales
            total_taxed_income = taxes.calculate_taxed_income()
            total_taxable_income = taxes.calculate_taxable_income()
            total_deductions = taxes.calculate_deductions()
            total_income_taxes = taxes.calculate_total_taxes()

            # Actualizar etiquetas de resultados
            self.taxed_income_label.text = f"The total amount of taxed income is: ${total_taxed_income}"
            self.taxable_income_label.text = f"The total amount of untaxed income is: ${total_taxable_income}"
            self.deductions_label.text = f"The total amount of deductions is: ${total_deductions}"
            self.income_taxes_label.text = f"TThe total amount of taxes to be paid is: ${total_income_taxes}"

        except (InsufficientLaborIncome, CommaSeparator, NotAnIntegerValue, NegativeTaxes, InsufficientIncome,
                ZeroSocialSecurityPayments, NegativeValue, NegativeWithholdingTaxes, EducationExpensesGreaterthanLaborIncome,
                EducationExpensesGreaterThanTotalIncome, DonationsGreaterThanLaborIncome, MortgageLosnPaymentsGreaterThanLaborIncome,
                PensionContributionGreaterThanLaborIncome, SocialSecurityPaymentsGreaterThanLaborIncome, LaborIncomeLessThanZero,
                InvalidValue) as error:
            self.mostrar_error(str(error))
        except ValueError:
            self.mostrar_error("The entered value is not in a correct format.\nPlease enter only numbers and use a period as decimal separator")

    def mostrar_error(self, mensaje_error):
        contenedor1 = BoxLayout(orientation='vertical')

        # Añadir la imagen
        imagen = Image(source='src\GUI\Images\precaution.png', size_hint=(1, 2))  # Ajusta el tamaño según necesites
        contenedor1.add_widget(imagen)

        mensaje = Label(text=mensaje_error, color=(1, 1, 1, 1))
        contenedor1.add_widget(mensaje)

        cerrar = Button(text="Close (X)", size_hint_y=None, height=30,background_color=(1, 0.5, 0.4, 1), color=(1, 1, 1, 1), bold=True)
        contenedor1.add_widget(cerrar)

        ventana = Popup(title="*** ERROR ***", content=contenedor1, size_hint=(0.9, 0.5))
        cerrar.bind(on_press=ventana.dismiss)
        ventana.open()

if __name__ == '__main__':
    TaxesCalculatorApp().run()

