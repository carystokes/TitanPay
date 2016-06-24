
from src.accounting.address import Address

class Employee:

    def __init__(self, emp_id, lname, fname, dues, pay_method, st_address, city, state, zip_code):
        self.__employee_id = emp_id
        self.__first_name = fname
        self.__last_name = lname
        self.__weekly_dues = dues
        self.__pay_method = pay_method
        self.__address = Address(st_address, city, state, zip_code)
        self.__full_address = st_address + ", " + city + ", " + state + " " + zip_code

    def get_full_name(self):
        full_name = self.__first_name + " " + self.__last_name
        return full_name

    def get_dues(self):
        return self.__weekly_dues

    def get_pay_method(self):
        return self.__pay_method

    def get_full_address(self):
        return self.__full_address


