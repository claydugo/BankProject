import mysql.connector
from credentials import *

"""
I couldn't get this to work correctly in this current form. 
Set u and p to your username and password in a file called credentials.py in the same directory.
From:
https://www.w3schools.com/python/python_mysql_getstarted.asp
"""

mydb = mysql.connector.connect(
  host="satoshi.cis.uncw.edu",
  user=u,
  password=p
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
