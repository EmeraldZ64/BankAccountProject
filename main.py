# TODO: IMPORT SUBCLASSES WHEN FINISHED


from SavingsAccountClass import SavingsAccount
from CheckingAccountClass import CheckingAccount

def main():
    # TODO: CREATE INSTANTIATIONS OF CHECKING AND SAVINGS ACCOUNT (2 EACH) FOR TESTING

    jeff_checking = CheckingAccount("Jeff",600,10)
    john_checking = CheckingAccount("John", 20000, 1001)

    jeff_checking.transfer(20)
    john_checking.transfer(500)
    jeff_checking.print_customer_info()
    john_checking.print_customer_info()
    pass

if "__main__" == __name__:
    main()
