from src.accounting.employee import Employee
from src.accounting.timecard import TimeCard
import datetime

class HourlyEmployee(Employee):

    def __init__(self, emp_id, fname, lname, hrly_rt, dues):
        Employee.__init__(self, emp_id, fname, lname, dues)
        self.__hourly_rate = hrly_rt
        self.__TimeCards = []

    def clockin(self):
        now = datetime.datetime.now()
        nowstr = str(now)
        timecard_date = nowstr[0:9]
        st_time = nowstr[11:13] + nowstr[14:16]
        end_time = ""
        tcard = TimeCard(timecard_date,st_time, end_time)
        self.__TimeCards.insert(0, tcard)

    def clockout(self):
        now = datetime.datetime.now()
        nowstr = str(now)
        end_time = nowstr[11:13] + nowstr[14:16]
        self.__TimeCards[0].set_end_time(self, end_time)

    def calc_pay(self, st_date, end_date): # Assume date format of string YYYY-MM-DD
        start = 0
        end = 0

        for i in range(0, len(self.__TimeCards)):
            if end == 0:
                tcard = self.__TimeCards[i]
                date = tcard.get_date(self)

                if end_date[i] != date:
                    break

                else:
                    end = i
            else:
                break

        for i in range(end, len(self.__TimeCards)):
            if start == 0:
                tcard = self.__TimeCards[i]
                date = tcard.get_date(self)

                if st_date[i] != date:
                    break

                else:
                    start = i
            else:
                break

        pay = 0
        for k in range(end, start + 1):
            tcard = self.__TimeCards[k]
            pay += tcard.calculate_daily_pay(self)

        dues = Employee.get_dues(self)
        pay -= dues

        return pay


