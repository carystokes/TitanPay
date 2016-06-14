from src.accounting.employee import Employee
from src.accounting.receipt import Receipt
import datetime

class SalariedEmployee(Employee):

    def __init__(self, emp_id, fname, lname, sal, comm_rate, dues):
        Employee.__init__(self, emp_id, fname, lname, dues)

        self.__salary = sal
        self.__commission_rate = comm_rate
        self.__receipts = []

    def makesale(self, amt):
        now = datetime.datetime.now()
        nowstr = str(now)
        rec_date = nowstr[0:10]
        receipt = Receipt(rec_date, amt)
        self.__receipts.insert(0, receipt)

    def pay(self, st_date, end_date):
        pay = 0
        st_day = st_date[9:]
        st_month = st_date[6:8]
        end_day = end_date[9:]
        end_month = end_date[6:8]
        if end_month == st_month:
            for i in range(0, len(self.__receipts)):
                receipt = self.__receipts[i]
                rec_date = receipt.get_date()
                rec_day = rec_date[9:]
                rec_month = rec_date[6:8]
                if rec_month == end_month:
                    if rec_day >= st_day and rec_day <= end_day:
                        amount = receipt.get_amt()
                        pay += self.__commission_rate * amount
                    else:
                        continue
                else:
                    continue

        else:
            for i in range(0, len(self.__receipts)):
                receipt = self.__receipts[i]
                rec_date = receipt.get_date()
                rec_day = rec_date[9:]
                rec_month = rec_date[6:8]
                if rec_month == end_month:
                    if rec_day <= end_day:
                        amount = receipt.get_amt()
                        pay += self.__commission_rate * amount
                    else:
                        continue
                else:
                    continue
            for i in range(0, len(self.__receipts)):
                receipt = self.__receipts[i]
                rec_date = receipt.get_date()
                rec_day = rec_date[9:]
                rec_month = rec_date[6:8]
                if rec_month == st_month:
                    if rec_day >= st_day:
                        amount = receipt.get_amt()
                        pay += self.__commission_rate * amount
                    else:
                        continue
                else:
                    continue

        months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 30, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        days = 0
        if st_month == end_month:
            days = end_day - st_day
        else:
            st_mon_days = months[st_month]
            days += st_mon_days - st_day + end_day

        pay += days / 365 * self.__salary
        dues = Employee.get_dues(self)
        adjusted_dues = dues * days / 7
        pay -= adjusted_dues

        return pay
