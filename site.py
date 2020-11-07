from flask import Flask, render_template, request, json
import mysql.connector
from credentials import *
app = Flask(__name__)

mydb = mysql.connector.connect(
  host="satoshi.cis.uncw.edu",
  user=u,
  password=p, 
  database ="narayanFall2020group3"
)

mycursor = mydb.cursor()

@app.route("/")
def main():
    return render_template('Main.html')

@app.route("/showadminfunctions")
def showadminfunctions():
    return render_template('index.html')

@app.route("/showcustomerfunctions")
def showcustomerfunctions():
    return render_template('customerfunctions.html')

@app.route("/showreportfunctions")
def showreportfunctions():
    return render_template('reportfunctions.html')


@app.route('/showcustomer')
def showcustomer():
    return render_template('customer.html')

@app.route('/employees')
def showemployees():
    return render_template('employees.html')



@app.route('/getemployees', methods=['GET','POST'])
def login():
    c=str((request.form['city']))
    print(c)
    if(c == "Montauk"):
           print("Done")
    return render_template('form.html')

if __name__ == "__main__":
    app.run()
