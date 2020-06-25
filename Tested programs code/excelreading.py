import xlrd
#create obj of workbook

wk = xlrd.open_workbook("C:/DRIVE DATA/xlrd.xlsx")
print(wk.nsheets)
#move sheet level

#ws=wk.sheet_by_index(1)
ws=wk.sheet_by_name("Sheet1")
#print(ws.nrows)
#print(ws.ncols)

#accesing cell and value

wc=ws.cell(0,0)

print(wc.value)

wc=ws.cell(2,1)
print(wc.value)


