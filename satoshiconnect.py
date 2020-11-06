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

def listResult(result):
    lst = []
    for i in result:
        lst.append([i])

        
mycursor = mydb.cursor()

mycursor.execute("SHOW tables")

tables = listResult(mycursor)

# print tables
for i in tables:
    mycursor.execute(f"SELECT * FROM {i}")
    result = listResult(mycursor.fetchall())
    print(result)
    print('-'*25)
