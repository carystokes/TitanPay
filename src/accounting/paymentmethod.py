from src.accounting.address import Address
from src.accounting.mailpayment import MailPayment
from src.accounting.pickuppayment import PickUpPayment
from src.accounting.directdepositpayment import DirectDepositPayment

class PaymentMethod:

    def __init__(self, pay_method, pay):
        self.__payment_method = pay_method
        self.__pay = pay

    def pay(self, pay_method, pay):
        if self.__payment_method == 0:
            self.address = Address.get_address(self)
            output = MailPayment.pay(pay, pay_method, self.address)

        elif self.__payment_method == 1:
            output = PickUpPayment.pay(pay, pay_method)

        else:
            output = DirectDepositPayment.pay(pay, pay_method)

        print(output)
