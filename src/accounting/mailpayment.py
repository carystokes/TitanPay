from src.accounting.paymentmethod import PaymentMethod

class MailPayment(PaymentMethod):
    def __init__(self, pay, address):
        PaymentMethod.__init__(self)
        self.__pay = pay
        self.__address = address

    def pay(self):
        output = "Mailing a check to Adrian Tillman for $", str(format(self.__pay, ',.2f')), " to ", self.__address


