from src.accounting.bankaccount import BankAccount
from src.accounting.paymentmethod import PaymentMethod


class DirectDepositPayment(PaymentMethod):
    def __init__(self, pay):
        PaymentMethod.__init__(self)
        self.pay = pay

    def pay(self):
        output = BankAccount.deposit(self, self.pay)
        return output
