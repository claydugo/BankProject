import mysql.connector
from credentials import *
import os
import time


class Menu:
    def __init__(self, label, options):
        self.label = label
        self.options = options

    def __str__(self):
        os.system('clear')
        printHeader(self.label)
        printable = ''
        menuNum = 0
        for i in self.options:
            menuNum += 1
            printable += f'{menuNum}) {i}\n'
        return printable


def printHeader(inner):
    print('-'*20)
    print(inner)
    print('-'*20)


def mainMenu():
    opt = ['Manage Accounts', 'Manage Employees', 'Placeholder']
    main = Menu('Command Line Bank', opt)
    print(main)
    uSelec = int(input(f'Select an option from 1 - {len(opt)}\n'))
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
            mainMenu()


def menuExec(uSelec):
    if uSelec == 1:
        accountManagement()
        return
    elif uSelec == 2:
        employeeManagement()
        return
        # Deposit
    elif uSelec == 3:
        mainMenu()
        return
    elif uSelec == 4:
        getName()
        return
    elif uSelec == 5:
        getBalance()
        return
    elif uSelec == 6:
        getCustomerCity()
        return
    elif uSelec == 7:
        listEmployees()
        return
    elif uSelec == 8:
        openAccount()
        return
    else:
        raise Exception


def accountManagement():
    menuBuffer = 3
    opt = ['Get Name', 'Get Balance', 'Get City']
    account = Menu('Command Line Bank Account Menu', opt)
    print(account)
    uSelec = int(input(f'Select an option from 1 - {len(opt)}\n'))
    menuNav(menuBuffer+uSelec)


def employeeManagement():
    menuBuffer = 6
    opt = ['List Employees', 'Open Account', 'Create Loan']
    account = Menu('Command Line Bank Employee Menu', opt)
    print(account)
    uSelec = int(input(f'Select an option from 1 - {len(opt)}\n'))
    menuNav(menuBuffer+uSelec)


def navBack():
    ans = input('Would you like to navigate back to the main menu? Y/N\n')
    if ans == 'Y' or ans == 'y':
        mainMenu()
        return
    elif ans == 'N' or ans == 'n':
        time.sleep(1)
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


def getName():
    accID = input('Please enter the account ID\n')
    mydb = initializeDB()
    c = mydb.cursor()
    c.execute(
        f'select cust_name from customer,account where customer.acc_id = {accID} and account.acc_id = {accID}')
    try:
        res = c.fetchall()
        name = res[0][0]
        print(name)
        navBack()
    except:
        print(f'Invalid entry, navigating you back to the main menu')
        time.sleep(2)
        mainMenu()


def getBalance():
    accID = input('Please enter the account ID\n')
    mydb = initializeDB()
    c = mydb.cursor()
    c.execute(f'select balance from account where acc_id = {accID}')
    try:
        res = c.fetchall()
        bal = res[0][0]
        print(bal)
        navBack()
    except:
        print(f'Invalid entry, navigating you back to the main menu')
        time.sleep(2)
        mainMenu()


def getCustomerCity():
    accID = input('Please enter the account ID\n')
    mydb = initializeDB()
    c = mydb.cursor()
    c.execute(
        f'select cust_city from customer,account where customer.acc_id = {accID} and account.acc_id = {accID}')
    try:
        res = c.fetchall()
        print(res[0][0])
        navBack()
        return
    except:
        print(f'Invalid entry, navigating you back to the main menu')
        time.sleep(2)
        mainMenu()


def listEmployees():
    mydb = initializeDB()
    c = mydb.cursor()
    c.execute(f'select distinct emp_city from employee;')
    res = c.fetchall()
    print('Please enter the name of the city you wish to list employees for')
    for i in range(0, len(res)):
        print(res[i][0])
    a = input('')
    c.execute(
        f'select emp_name, pho_num from employee where emp_city = \'{a}\';')
    r2 = c.fetchall()
    printHeader(f'{a} Branch')
    for i in range(0, len(r2)):
        print(f'Name: {r2[i][0]}\t Phone#: {r2[i][1]}')
    navBack()


def openAccount():
    mydb = initializeDB()
    c = mydb.cursor()
    c.execute(f'select max(acc_id) from account where acc_type = \'User\'')
    res = c.fetchall()
    aAccID = int(res[0][0]) + 1
    aType = 'User'
    aName = input('Please enter the full name of the account holder\n')
    aCity = input('Please enter the city of the account holder\n')
    aBal = input('Please enter the starting balance of the account holder\n')
    cID = aAccID + 100
    c.execute(f'insert into account values({aAccID}, {aBal}, \'{aType}\')')
    c.execute(f'insert into customer values({cID}, \'{aName}\', \'{aCity}\', {aAccID})')
    mydb.commit()
    navBack()

if __name__ == '__main__':
    mainMenu()
