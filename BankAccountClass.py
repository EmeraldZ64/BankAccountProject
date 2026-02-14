import random

class BankAccount:

    bankName = "Fells Wargo"
    # private 9 digit variable for bank's routing number, same across all accounts
    __routing_number = random.randint(111111111,999999999)

    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

        # protected 8 digit variable for account number, random for each account
        self._account_number = random.randint(11111111, 99999999)

    def deposit(self, amt):
            self.balance += amt

    def withdraw(self, amt):
        if self.validate_balance(amt):
            self.balance -= amt

    def print_customer_info(self):
        print("Bank Name: ", self.bankName)
        print("Account Owner: ", self.name)
        print("Balance: ", self.balance)
        print("Minimum Balance: ", self.min_balance)
        print("Account Number: ", self._account_number)
        print("Routing Number: ", self.__routing_number)

    def validate_balance(self, amt):
        if self.balance - amt < self.min_balance: # if subtracting amount leads to lower than minimum balance
            return False
        else:
            return True