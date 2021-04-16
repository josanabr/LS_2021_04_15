import gspread
from flask import Flask, request, jsonify

app = Flask(__name__)
gc = gspread.service_account(filename="/workdir/demo-ls.json")
sh = gc.open("DEMO-LS")

@app.route("/")
def A1():
  if request.json:
    print(request.json['saludo'])
  return sh.sheet1.cell(1,1).value

@app.route("/obtenervalor",methods=['POST'])
def obtenervalor():
  row = request.json['row']
  col = request.json['col']
  return sh.sheet1.cell(row, col).value

if  __name__ == '__main__':
  app.run(host='0.0.0.0')
