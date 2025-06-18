
from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withDraw(self, amount):
        pass

class SavingAccount(Account):

    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited: ", amount)

    def withDraw(self, amount):
        if self.__balance < amount:
            print("Not Enough Balance")
            return
        self.__balance -= amount
        print("Amount withdrawn: ", amount)

class CurrentAccount(Account):

    def __init__(self, limit):
        self.__balance = 0
        self.withDraw_limit = limit

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited: ", amount)

    def withDraw(self, amount):
        if self.__balance + self.withDraw_limit < amount:
            print("Not Enough Balance")
            return
        self.__balance -= amount
        print("Amount withdrawn: ", amount)

class Bank:

    def __init__(self, name, number, account_type="Saving"):
        self.owner = name
        self.account_number = number

        if account_type == "Saving":
            self.account = SavingAccount()
        elif account_type == "Current":
            self.account = CurrentAccount(5000)
        else:
            raise ValueError("Invalid account type")

class Manager:
    def get_customer_info(self , bankAccount : Bank):
        print(f"Name : {bankAccount.owner}")
        print(f"AccountNumber : {bankAccount.account_number}")
        print("Account Type : ", end="")
        if(type(bankAccount.account) == SavingAccount):
            print("Savings Account")
        else:
            print("Current Account")
        print(f"Balance : {bankAccount.account.get_balance()}")

    def __str__(self):
        return "Manager Object "

# Main
manager = Manager()
accounts = {}

while True:
    print("\n Bank Application")
    print("1.Create Account")
    print("2. Account Details")
    print("3. Deposit Amount")
    print("4. withdraw Amount")
    print("5.Exit from bank")
    n=int(input("Enter the choice: "))
    if n==1:
        name = input("Enter acc holder name: ")
        number = input("Enter acc number: ")
        acc_type = input("Enter acc type : ")
        accounts[number] = Bank(name, number, acc_type)
    elif n==2:
        acc_number = input("Enter acc number to view details: ")
        #account_name = input("Enter acc name to view details: ")
        if acc_number in accounts:
            manager.get_customer_info(accounts[acc_number])
        else:
            print("Acc not found")
    elif n==3:
        acc_number = input("Enter acc number to deposit: ")
        if acc_number in accounts:
            amount = int(input("Enter amount to deposit: "))
            accounts[acc_number].account.deposit(amount)
        else:
            print("Acc not found")

    elif n==4:
        acc_number = input("Enter acc number to withdraw: ")
        if acc_number in accounts:
            amount = int(input("Enter amount to withdraw: "))
            accounts[acc_number].account.withDraw(amount)
        else:
            print("Acc not found")
    elif n==5:
        print("Exiting the program")
        break
    else:
        print("Invalid")
