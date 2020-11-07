import mysql.connector
from credentials import *
import os
import time

class Menu:
    def __init__(self, label, options, previous):
        self.label = label
        self.options = options
        self.previous = previous

    def __str__(self):
        os.system('clear')
        print(self.label)
        printable = ''
        menuNum = 0
        for i in self.options:
            menuNum += 1
            printable += f'{menuNum}) {i}\n'
        return printable


def mainMenu():
    opt = ['Get Balance', 'Deposit', 'List Employees']
    main = Menu('Command Line Bank', opt, 'placeholder')
    print(main)
    uSelec = input(f'Select an option from 1 - {len(opt)}\n')
    menuNav(uSelec)


def menuNav(uSelec):
    if uSelec == '':
        mainMenu()
    else:
        try:
            menuExec(uSelec)
        except ValueError:
            print('Invalid Entry, navigating back to main menu')
            time.sleep(1)

def menuExec(uSelec):
    if uSelec == '1':
        getBalance()
        return
    elif uSelec == '2':
        mainMenu()
        print('Would execute Deposit')
        return
        # Deposit
    elif uSelec == '3':
        listEmployees()
        return
    elif uSelec == '4':
        mainMenu()
        print('Would execute yada')
        #yada
        return
    else:
        print('else lol')


def navBack():
    ans = input('Would you like to navigate back to the main menu? Y/N\n')
    if ans == 'Y' or ans == 'y':
        mainMenu()
        return
    elif ans == 'N' or ans == 'n':
        exit()
    else:
        navBack()
        return

def initializeDB():
    mydb = mysql.connector.connect(
      host="satoshi.cis.uncw.edu",
      user=u,
      password=p,
      database="narayanFall2020group3"
    )
    return mydb

def getBalance():
    accID = input('Please enter your account ID\n')
    mydb = initializeDB()
    c = mydb.cursor()
    c.execute(f'select balance from account where acc_id = {accID}')
    res = c.fetchall()
    bal = res[0][0]
    print(bal)
    navBack()

def listEmployees():
    mydb = initializeDB()
    c = mydb.cursor()
    c.execute(f'select distinct emp_city from employee;')
    res = c.fetchall()
    print('Please enter the name of the city you wish to list employees for')
    for i in range(0, len(res)):
        print(res[i][0])
    a = input('')
    c.execute(f'select emp_name, pho_num from employee where emp_city = \'{a}\';')
    r2 = c.fetchall()
    print('-'*20)
    print(f'{a} Branch')
    print('-'*20)
    for i in range(0, len(r2)):
        print(f'Name: {r2[i][0]}\t Phone#: {r2[i][1]}')

if __name__ == '__main__':
    mainMenu()

