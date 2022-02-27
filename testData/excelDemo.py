import openpyxl as openpyxl

book = openpyxl.load_workbook("C:\\work\\PythonSel.xlsx")

sheet = book.active

cell = sheet.cell(row=2, column=2)

print(cell.value)

#cell.value  = "TK"


print(cell.value)
