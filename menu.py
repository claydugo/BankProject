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


def mainMenu():
    opt = ['Manage Accounts', 'Manage Employees', 'Transaction History']
    main = Menu('Command Line Bank', opt)
    print(main)
    uSelec = int(input(f'Select an option from 1 - {len(opt)}\n'))
    print(uSelec)
    if uSelec == 1:
        accountManagement()
        return
    elif uSelec == 2:
        employeeManagement()
        return
        # Deposit
    elif uSelec == 3:
        transactionMenu()
        return






def accountManagement():
    opt = ['Get Name', 'Get Balance', 'Get City', 'Open Account','Deposit','Withdraw','Transfer']
    account = Menu('Command Line Bank Account Menu', opt)
    print(account)
    uSelec = int(input(f'Select an option from 1 - {len(opt)}\n'))
    print(uSelec)
    if uSelec == 1:
        getName()
    elif uSelec == 2:
        getBalance()
    elif uSelec == 3:
        getCustomerCity()
    elif uSelec == 4:
        openAccount()
    elif uSelec == 5:
        deposit()
    elif uSelec == 6:
        withdraw()
    elif uSelec == 7:
        transfer()
    navBack()




def employeeManagement():
    opt = ['List Employees', 'Open Account', 'Create Loan']
    account = Menu('Command Line Bank Employee Menu', opt)
    print(account)
    uSelec = int(input(f'Select an option from 1 - {len(opt)}\n'))
    print(uSelec)

    if uSelec == 1:
        listEmployees()
    elif uSelec == 2:
        print("Will add more functions later -Clay")
    navBack()

def transactionMenu():
    opt = ['Create Save Point', 'Rollback to a previous version']
    menu = Menu('Command Line Bank Transaction History Menu',opt)
    print(menu)
    uSelec = int(input(f"Select option from 1 - {len(opt)}\n"))
    print(uSelec)
    if uSelec == 1:
        createSavepoint()
    elif uSelec == 2:
        rollBack()
    navBack()



def initializeDB():
    mydb = mysql.connector.connect(
        host="satoshi.cis.uncw.edu",
        user=u,
        password=p,
        database="narayanFall2020group3"
    )
    return mydb

def createSavepoint():
    mydb = initializeDB()
    c = mydb.cursor()
    saveName = input("Enter a savepoint name for this version of the data base")
    c.execute("START TRANSACTION;")
    c.execute(f"SAVEPOINT {saveName};")
    mydb.commit()
def rollBack():
    mydb = initializeDB()
    c = mydb.cursor()
    saveName = input("Enter the saveName of the save you want to rollback")
    c.execute(f"ROLLBACK TO {saveName};")
    mydb.commit()


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

def getBalanceo(accID):
    mydb = initializeDB()
    c = mydb.cursor()
    c.execute(f'select balance from account where acc_id = {accID}')
    res = c.fetchall()
    return res[0][0]

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
    print(res)
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

def deposito(accID,amount):
    mydb = initializeDB()
    c = mydb.cursor()
    oldBal = getBalanceo(accID)
    newBal = oldBal + amount
    c.execute(f"update account set balance = {newBal} where acc_id = " + str(accID))
def deposit():
    mydb = initializeDB()
    c = mydb.cursor()
    accID = int(input("Enter Account ID for the recipient of the deposit: "))
    amount = int(input("Amount to deposit: "))
    oldBal = getBalanceo(accID)
    newBal = oldBal + amount
    c.execute(f"update account set balance = {newBal} where acc_id = " + str(accID))
    mydb.commit()
    updatedBal = getBalanceo(accID)
    print("Old Balance: " + str(oldBal))
    print("New Balance: " + str(updatedBal))
def withdraw():
    mydb = initializeDB()
    c = mydb.cursor()
    accID = int(input("Enter Account ID for the recipient of the withdraw: "))
    amount = int(input("Amount to withdraw: "))

    oldBal = getBalanceo(accID)
    if(amount > oldBal):
        print("Insufficient funds")
        return False
    else:
        newBal = oldBal - amount
        c.execute(f"update account set balance = {newBal} where acc_id = " + str(accID))
        mydb.commit()
        print("Old Balance: " + str(oldBal))
        print("New Balance: " + str(getBalanceo(accID)))
        return True
def withdrawo(accID,amount):
    mydb = initializeDB()
    c = mydb.cursor()
    oldBal = getBalanceo(accID)
    if(amount > oldBal):
        print("Insufficient funds")

        return False
    else:
        newBal = oldBal - amount
        c.execute(f"update account set balance = {newBal} where acc_id = " + str(accID))
        mydb.commit()
        return True
def transfero(accIDfrom,accIDto,amount):
    mydb = initializeDB()
    c = mydb.cursor()
    try:
        if (withdrawo(accIDfrom, amount)):

            deposito(accIDto, amount)
        else:
            print("Insufficient Funds")
    except:
        print("one of the accounts do not exist")
def transfer():
    mydb = initializeDB()
    c = mydb.cursor()
    accIDfrom = int(input("Enter the source account for the transfer: "))
    accIDto = int(input("Enter the recipient account for the transfer: "))
    amount = int(input("Enter the amount to transfer: "))
    try:
        if(withdrawo(accIDfrom,amount)):

            deposito(accIDto,amount)
        else:
            print("Insufficient Funds")

    except:
        print("one of the accounts do not exist")



if __name__ == '__main__':
    mainMenu()
