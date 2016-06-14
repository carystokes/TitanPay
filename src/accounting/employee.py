from src.accounting.paymentmethod import PaymentMethod

class Employee:

    def __init__(self, emp_id, fname, lname, dues, pay_method):
        self.__employee_id = emp_id
        self.__first_name = fname
        self.__last_name = lname
        self.__weekly_dues = dues
        self.__pay_method = pay_method

    def get_full_name(self):
        full_name = self.__last_name + ", " + self.__first_name
        return full_name

    def get_dues(self):
        return self.__weekly_dues

    def get_pay_method(self):
        return self.__pay_method

    def process_payment(self, pay_method, pay):
        PaymentMethod.pay(pay_method, pay)
