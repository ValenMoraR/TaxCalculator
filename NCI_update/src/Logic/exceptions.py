class NonNumericValueError(Exception):
    """Excepción lanzada cuando se ingresa un valor no numérico."""
    pass

'''For when the value of labor income is lower'''
class InsufficientLaborIncome(Exception):
    pass

'''For when there are negative values'''
class NegativeValue(Exception): 
    pass

'''For when characters other than numbers are entered'''
class InvalidValue(Exception): 
    pass

'''For when labor income is negative'''
class LaborIncomeLessThanZero(Exception):
    pass

'''When social security is worth more than labor income'''
class SocialSecurityPaymentsGreaterThanLaborIncome(Exception):
    pass

'''For when pension contributions have a value greater than labor income'''
class PensionContributionGreaterThanLaborIncome(Exception):
    pass

'''When will mortgage payments be worth more than labor income'''
class MortgageLosnPaymentsGreaterThanLaborIncome(Exception):
    pass

'''For when donations are worth more than labor income'''
class DonationsGreaterThanLaborIncome(Exception):
    pass

'''When education expenditures are worth more than total income'''
class EducationExpensesGreaterThanTotalIncome(Exception):
    pass

'''When education expenses are worth more than labor income'''
class EducationExpensesGreaterthanLaborIncome(Exception):
    pass

'''For when the source withholding is negative'''
class NegativeWithholdingTaxes(Exception):
    pass

class ZeroSocialSecurityPayments(Exception):
    pass

class InsufficientIncome(Exception):
    pass

class NegativeTaxes(Exception):
    pass

class NotAnIntegerValue(Exception):
    pass

class CommaSeparator(Exception):
    pass

