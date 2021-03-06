from src.accounting.employee import Employee
from src.accounting.receipt import Receipt
from src.accounting.mailpayment import MailPayment
from src.accounting.pickuppayment import PickUpPayment
from src.accounting.directdepositpayment import DirectDepositPayment


class SalariedEmployee(Employee):

    def __init__(self, emp_id, lname, fname, sal, comm_rate, dues, pay_method, st_address, city, state, zip):
        Employee.__init__(self, emp_id, lname, fname, dues, pay_method, st_address, city, state, zip)

        self.__salary = float(sal)
        self.__commission_rate = float(comm_rate) / 100
        self.__receipts = []

    def create_receipt(self, emp_id, lname, item, units, unit_cost, total):
        receipt = Receipt(emp_id, lname, item, units, unit_cost, total)
        self.__receipts.append(receipt)
        return

    def get_number_receipts(self):
        return len(self.__receipts)

    def calc_pay(self):
        pay_amt = 0
        for i in self.__receipts:
            pay_amt += i.get_pay_data() * self.__commission_rate

        pay_amt += self.__salary / 12
        dues = Employee.get_dues(self)
        pay_amt -= float(dues)

        full_name = Employee.get_full_name(self)
        if Employee.get_pay_method(self) == 'MA':
            full_address = Employee.get_full_address(self)
            mpayment = MailPayment(pay_amt, full_name, full_address)
            output = mpayment.get_output()

        elif Employee.get_pay_method(self) == 'PU':
            ppayment = PickUpPayment(pay_amt, full_name)
            output = ppayment.get_output()

        else:
            dpayment = DirectDepositPayment(pay_amt, full_name)
            output = dpayment.get_output()

        return output

