from src.accounting.employee import Employee
from src.accounting.timecard import TimeCard
from src.accounting.mailpayment import MailPayment
from src.accounting.pickuppayment import PickUpPayment
from src.accounting.directdepositpayment import DirectDepositPayment


class HourlyEmployee(Employee):

    def __init__(self, emp_id, lname, fname, hrly_rt, dues, pay_method, st_address, city, state, zip_code):
        Employee.__init__(self, emp_id, lname, fname, dues, pay_method, st_address, city, state, zip_code)
        self.__hourly_rate = hrly_rt
        self.__timeCards = []

    def clockin(self, timecard_date, st_time):
        end_time = ""
        tcard = TimeCard(timecard_date, st_time, end_time)
        self.__timeCards.append(tcard)

    def get_timeCard_length(self):
        return len(self.__timeCards)

    def clockout(self, timecard_date, end_time):
        for i in self.__timeCards:
            if i.get_tcdate() == timecard_date:
                i.set_end_time(end_time)

    def get_timeCard_end_time(self):
        return self.__timeCards[0].end_time

    def calc_pay(self):

        pay_total = 0
        for tcard in self.__timeCards:
            pay_total += tcard.calculate_daily_pay(self.__hourly_rate)

        if pay_total > 0:
            dues = float(Employee.get_dues(self))
            pay_total -= dues
        else:
            return -1

        full_name = Employee.get_full_name(self)
        if Employee.get_pay_method(self) == 'MA':
            full_address = Employee.get_full_address(self)
            mpayment = MailPayment(pay_total, full_name, full_address)
            output = mpayment.get_output()

        elif Employee.get_pay_method(self) == 'PU':
            ppayment = PickUpPayment(pay_total, full_name)
            output = ppayment.get_output()

        else:
            dpayment = DirectDepositPayment(pay_total, full_name)
            output = dpayment.get_output()

        return output


