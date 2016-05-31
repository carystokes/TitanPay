class Employee:
    def __init__(self, emp_id, first_name, last_name, hourly_rate, dues):
        self.__employee_id = emp_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__hourly_rate = float(hourly_rate)
        self.__weekly_dues = float(dues)

    def get_full_name(self):
        __full_name = self.__last_name + ", " + self.__first_name
        return __full_name
