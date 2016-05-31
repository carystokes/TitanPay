class Employee:

    def __init__(self, emp_id, fname, lname, hrly_rt, dues):
        self.__employee_id = emp_id
        self.__first_name = fname
        self.__last_name = lname
        self.__hourly_rate = float(hrly_rt)
        self.__weekly_dues = float(dues)

    def get_full_name(self):
        full_name = self.__last_name + ", " + self.__first_name
        return full_name
