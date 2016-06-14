from src.accounting.bankaccount import BankAccount
from src.accounting.paymentmethod import PaymentMethod

class DirectDepositPayment(PaymentMethod):
    def __init__(self, pay_method, pay):
        self.pay = pay

    def pay(self, pay_method, pay):
        output = BankAccount.deposit(self, pay)
        return output
