import xlrd
xlsfile = xlrd.open_workbook('SkillCheck.xlsx')
sheet = xlsfile.sheet_by_index(0)
print(sheet.cell_value(0,0))
print(sheet.ncols,sheet.ncols)
print(sheet.col_values(0)[1:])