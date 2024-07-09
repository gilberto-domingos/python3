import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Creating an instance of Faker with Brazilian locale
fake = Faker('pt_BR')

# Functions to generate unique data
def generate_company():
    suffixes = ['ME', 'EPP', 'GE']
    return f'{fake.company()} - {random.choice(suffixes)}'

def generate_cnpj():
    return fake.cnpj()

def generate_title():
    return f'{random.randint(10000000, 99999999)}'

def generate_process_code():
    return f'P{random.randint(1000000000, 9999999999)}'

def generate_employee_code():
    return random.randint(1000, 9999)

def generate_sale():
    return f'R$ {round(random.uniform(100.0, 10000.0), 2)}'

def generate_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date).strftime('%d/%m/%Y')

# Ensuring the data is unique
companies = []
while len(companies) < 500:
    company = generate_company()
    if company not in companies:
        companies.append(company)

cnpjs = []
while len(cnpjs) < 500:
    cnpj = generate_cnpj()
    if cnpj not in cnpjs:
        cnpjs.append(cnpj)

titles = []
while len(titles) < 500:
    title = generate_title()
    if title not in titles:
        titles.append(title)

process_codes = []
while len(process_codes) < 500:
    process_code = generate_process_code()
    if process_code not in process_codes:
        process_codes.append(process_code)

employee_codes = []
while len(employee_codes) < 500:
    employee_code = generate_employee_code()
    if employee_code not in employee_codes:
        employee_codes.append(employee_code)

sales = []
while len(sales) < 500:
    sale = generate_sale()
    if sale not in sales:
        sales.append(sale)

dates = []
while len(dates) < 500:
    date = generate_date()
    if date not in dates:
        dates.append(date)

# Creating the DataFrame
data = {
    'Empresa': companies,
    'CNPJ': cnpjs,
    'Título': titles,
    'Processo': process_codes,
    'Funcionário': employee_codes,
    'Venda': sales,
    'Data': dates,
    'Comissão': [''] * 500  # Adding empty "Commission" column
}

df = pd.DataFrame(data)

# Saving to an Excel file in the current directory
file_path = 'files/com_sales.xlsx'
df.to_excel(file_path, index=False)
print(f'File saved as {file_path}')
