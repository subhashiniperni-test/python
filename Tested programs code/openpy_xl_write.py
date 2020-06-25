import openpyxl

wk=openpyxl.Workbook()
sh=wk.active
sh.title="First sheet"
sh['A1'].value="www. testingworld.com"

wk.create_sheet(title="Secondone")
sh1=wk['Secondone']
sh1['A2']="93434221134"
wk.remove(wk['First sheet'])
#print(sh.title)
wk.save("C:/DRIVE DATA/write1.xlsx")

