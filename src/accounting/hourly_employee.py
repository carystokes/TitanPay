from src.accounting.employee import Employee

class HourlyEmployee(Employee):

    def __init__(self, emp_id, fname, lname, hrly_rt, dues):
        Employee.__init__(self, emp_id, fname, lname)

        self.__hourly_rate = hrly_rt
        self.__weekly_dues = dues
