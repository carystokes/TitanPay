class SalariedEmployee:

    def __init__(self, emp_id, fname, lname, sal, comm_rate, dues):
        self.__employee_id = emp_id
        self.__first_name = fname
        self.__last_name = lname
        self.__salary = float(sal)
        self.__commission_rate = float(comm_rate)
        self.__weekly_dues = float(dues)

    def get_full_name(self):
        __full_name = self.__last_name + ", " + self.__first_name
        return __full_name