import xlrd

wk = xlrd.open_workbook("C:/DRIVE DATA/xlrd.xlsx")
ws=wk.sheet_by_index(0)
r=ws.nrows
c=ws.ncols

for i in range(0,r):
    for j in range(0,c):
        wc=ws.cell(i,j)
        print(wc.value)

