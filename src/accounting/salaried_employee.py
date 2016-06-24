from src.accounting.employee import Employee
from src.accounting.receipt import Receipt
from src.accounting.address import Address
from src.accounting.mailpayment import MailPayment
from src.accounting.pickuppayment import PickUpPayment
from src.accounting.directdepositpayment import DirectDepositPayment
import datetime

class SalariedEmployee(Employee):

    def __init__(self, emp_id, fname, lname, sal, comm_rate, dues, pay_method, st_address, city, state, zip):
        Employee.__init__(self, emp_id, fname, lname, dues, pay_method, st_address, city, state, zip)

        self.__salary = sal
        self.__commission_rate = comm_rate
        self.__receipts = []

    def makesale(self, amt):
        now = datetime.datetime.now()
        nowstr = str(now)
        rec_date = nowstr[0:10]
        receipt = Receipt(rec_date, amt)
        self.__receipts.append(receipt)

    def pay(self):
        pay_amt = 0
        for i in self.__receipts:
            pay_amt += i[1] * self.__commission_rate

        pay_amt += self.__salary / 12
        dues = Employee.get_dues(self)
        pay_amt -= dues

        self.payment(pay_amt)

    def payment(self, pay_amt):
        if self.__pay_method == 'MP':
            output = MailPayment.pay(pay_amt, self.address)

        elif self.__pay_method == 'PU':
            output = PickUpPayment.pay(pay_amt)

        else:
            output = DirectDepositPayment.pay(pay_amt)

        print(output)
