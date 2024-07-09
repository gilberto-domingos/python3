import openpyxl

workbook = openpyxl.load_workbook('../logic_exerc/files/clients_reg.xlsx')
sheet = workbook.active




'''
headers = [cell.value for cell in sheet[1]]
print('\t'.join(headers))

line_count = 0

for row in sheet.iter_rows(min_row=2, values_only=True):
    print('\t'.join(map(str, row)))
    line_count += 1
    if line_count == 3:
        break
'''