from src.accounting.bankaccount import BankAccount
from src.accounting.paymentmethod import PaymentMethod


class DirectDepositPayment(PaymentMethod):
    def __init__(self, pay_amt, full_name):
        PaymentMethod.__init__(self)
        self.__pay_amt = pay_amt
        self.__full_name = full_name

    def get_output(self):
        bankaccount = BankAccount('Bank of America', '001134567', '456456456456')
        output = bankaccount.deposit(self.__pay_amt, self.__full_name)
        return output
