# Project: Bank Account: Use of Class, init method, super keyword

"""
This Project you will learn 

 Use of Class, init method, self keyword, super keyword
 
"""
class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance


    def deposit(self, amount):
        self.balance +=  amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: £{}".format(self.balance))

"""
What is Super keyword?

Essentially, the super function can be used to gain access to inherited methods –
 from a parent or sibling class – that has been overwritten in a class object
 
"""

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 1000 )

    def __str__(self):
        return "{}'s Current Account : Balance £{}".format(self.name, self.balance)

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s Savings Account : Balance £{}".format(self.name, self.balance)

    
Z = Current("Ziad", 500)
Z.deposit(300)
Z.statement()
Z.withdraw(300)
Z.statement()



