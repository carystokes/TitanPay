from src.accounting.paymentmethod import PaymentMethod

class PickUpPayment(PaymentMethod):
    def __init__(self, pay_amt, name):
        PaymentMethod.__init__(self)
        self.__pay_amt = pay_amt
        self.__name = name

    def get_output(self):
        output = "A check for $" + str(format(self.__pay_amt, ',.2f')) + " is waiting for " + self.__name + " at the PostMaster."
        return output