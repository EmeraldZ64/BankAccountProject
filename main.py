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

    leon_savings = SavingsAccount("Leon",500,10)
    leon_savings.print_customer_info()
    leon_savings.pass_days(100)
    leon_savings.print_customer_info()

    claire_savings = SavingsAccount("Claire",5000,10)
    claire_savings.print_customer_info()
    claire_savings.pass_days(365)
    claire_savings.print_customer_info()

if "__main__" == __name__:
    main()
