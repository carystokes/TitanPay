class Employee:

    def __init__(self, emp_id, fname, lname):
        self.__employee_id = emp_id
        self.__first_name = fname
        self.__last_name = lname

    def get_full_name(self):
        full_name = self.__last_name + ", " + self.__first_name
        return full_name
