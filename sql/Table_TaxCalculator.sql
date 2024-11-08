create table taxcalculator (
  id int primary key not null,
  labor_income int not null,
  other_income int not null,
  social_security_contribution int not null ,
  pension_contribution int not null,
  mortgage_loan_payments int not null,
  donations int not null,
  education_expenses int not null,
  total_taxed_income int,
  total_taxable_income int,
  total_deductions int,
  total_income_taxes int
);

