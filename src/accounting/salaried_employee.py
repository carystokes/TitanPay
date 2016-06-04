from src.accounting.employee import Employee

class SalariedEmployee(Employee):

    def __init__(self, emp_id, fname, lname, sal, comm_rate, dues):
        Employee.__init__(self, emp_id, fname, lname)

        self.__salary = float(sal)
        self.__commission_rate = float(comm_rate)
        self.__weekly_dues = float(dues)

