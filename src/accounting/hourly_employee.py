from src.accounting.employee import Employee
from src.accounting.timecard import TimeCard
from src.accounting.address import Address
from src.accounting.mailpayment import MailPayment
from src.accounting.pickuppayment import PickUpPayment
from src.accounting.directdepositpayment import DirectDepositPayment
import datetime


class HourlyEmployee(Employee):

    def __init__(self, emp_id, fname, lname, hrly_rt, dues, pay_method):
        Employee.__init__(self, emp_id, fname, lname, dues, pay_method)
        self.__hourly_rate = hrly_rt
        self.__timeCards = []
        self.address = Address.get_address(self)

    def clockin(self):
        timecard_date, st_time = self.get_time()
        end_time = ""
        tcard = TimeCard(timecard_date, st_time, end_time)
        self.__timeCards.append(tcard)

    def clockout(self):
        timecard_date, end_time = self.get_time()
        for i in self.timeCards:
            if i[0] == timecard_date:
                self.__timeCards[i].set_end_time(self, end_time)

    def get_time(self):
        now = datetime.datetime.now()
        nowstr = str(now)
        date = nowstr[0:9]
        time = nowstr[11:13] + nowstr[14:16]
        return date, time

    def calc_pay(self):

        pay = 0
        for k in self.__timeCards:
            tcard = self.__timeCards[k]
            pay += tcard.calculate_daily_pay(self)

        dues = Employee.get_dues(self)
        pay -= dues

        pay(self, pay)

    def pay(self, pay):
        if self.__pay_method == 0:
            output = MailPayment.pay(pay, self.address)

        elif self.__pay_method == 1:
            output = PickUpPayment.pay(pay)

        else:
            output = DirectDepositPayment.pay(pay)

        print(output)


