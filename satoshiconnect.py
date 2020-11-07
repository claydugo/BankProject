import mysql.connector
from credentials import *

"""
This is working as intended
From:
https://www.w3schools.com/python/python_mysql_getstarted.asp
"""

mydb = mysql.connector.connect(
  host="satoshi.cis.uncw.edu",
  user=u,
  password=p,
  database="narayanFall2020group3"
)


mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


#returns balance for an account with accID
def getBalance(accID):
  try:
    mycursor.execute("select balance from account where acc_id = " + str(accID))
    res = mycursor.fetchall()
    bal = res[0][0]
    return bal
  except:
    return "account does not exist"

#returns the name associated with cusID
def getName(cusID):
  mycursor.execute("select cust_name from customer where cust_id = " + str(cusID))
  res = mycursor.fetchall()
  name = res[0][0]
  return name

def getAccountOwner(accID):
  mycursor.execute("select cust_name from customer,account where customer.acc_id = " + str(accID) + " and account.acc_id = " + str(accID))
  res = mycursor.fetchall()
  return res[0][0]

def getCustomerCity(cusID):
  mycursor.execute("select cust_city from customer where cust_id = " + str(cusID))
  res = mycursor.fetchall()
  return res[0][0]

def getEmployeeName(empID):
  mycursor.execute("select emp_name from employee where emp_id = " + str(empID))
  res = mycursor.fetchall()
  return res[0][0]

def getEmployeeCity(empID):
  mycursor.execute("select emp_city from employee where emp_id = " + str(empID))
  res = mycursor.fetchall()
  return res[0][0]

def getEmployeePhone(empID):
  mycursor.execute("select pho_num from employee where emp_id = " + str(empID))
  res = mycursor.fetchall()
  return res[0][0]

def deposit(accID,amount):
  oldBal = getBalance(accID)
  newBal = oldBal + amount
  mycursor.execute(f"update account set balance = {newBal} where acc_id = " + str(accID))

def withdraw(accID,amount):
  oldBal = getBalance(accID)
  if(amount > oldBal):
    return False
  else:
    newBal = oldBal - amount
    mycursor.execute(f"update account set balance = {newBal} where acc_id = " + str(accID))
    return True

def transfer(accIDfrom,accIDto,amount):
  try:
    if(withdraw(accIDfrom,amount)):
      deposit(accIDto,amount)
    else:
      return "Cannot complete transaction insufunds"
  except:
    print("one of the accounts do not exist")

def openAccount(accID,startingBal,accType,owner,ownercity,ownerid):
  mycursor.execute(f"insert into account values({accID},{startingBal},{accID})")
  mycursor.execute(f"insert into customer values({ownerid},\"{owner}\",\"{ownercity}\",{accID})")

print(getAccountOwner(201))
print(getBalance(201))
print(getBalance(202))
transfer(201,202,1000000000)

print(getBalance(201))
print(getBalance(202))

openAccount(1,100,"Cust","blah","Wilmington",2)