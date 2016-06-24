from src.accounting.paymentmethod import PaymentMethod

class MailPayment(PaymentMethod):
    def __init__(self, pay_amt, name, address):
        PaymentMethod.__init__(self)
        self.__pay_amt = pay_amt
        self.__address = address
        self.__name = name

    def get_output(self):
        output = "Mailing a check for $" + str(format(self.__pay_amt, ',.2f')) + " to " + self.__address \
                  + " for " + self.__name
        return output


