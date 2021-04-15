import gspread

gc = gspread.service_account()

sh = gc.open("DEMO-LS")

print(sh.sheet1.get('A1'))
