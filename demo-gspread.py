import gspread
from flask import Flask

app = Flask(__name__)
gc = gspread.service_account(filename="/workdir/demo-ls.json")
sh = gc.open("DEMO-LS")

@app.route("/")
def A1():
  return sh.sheet1.cell(1,1).value

if  __name__ == '__main__':
  app.run(host='0.0.0.0')
