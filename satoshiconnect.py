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
