#read excel file in python

import xlrd

loc = ("D:\\Python\\ExpertModule\\NewExcel.xls")

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)

print(sheet.cell_value(0,0))
print(sheet.ncols)
print(sheet.nrows)

for i in range(sheet.ncols):
    print(sheet.cell_value(0,1))

#to extract rpw value



