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

class Address:

    def __init__(self, st_add, city, state, zip_code):
        self.__street_address = st_add
        self.__city = city
        self.__state = state
        self.__zip = zip_code

    def get_address(self):
        full_address = self.__street_address + ", " + self.__city + ", " + self.__state + " " + self.__zip
        return full_address

class TimeCard:

    def __init__(self, date, st_time, end_time):
        self.__date = date
        self.__start_time = st_time
        self.__end_time = end_time

    def calculate_daily_pay(self, rate):
        import time
        # assuming time in HHMM format
        time_start = time.mktime(time.strptime("2016" + self.__start_time, "%Y%H%M"))
        time_end = time.mktime(time.strptime("2016" + self.__end_time, "%Y%H%M"))

        minutes = (int(time_end - time_start) / 60)

        if minutes > 480:
            reg_min = 480
            ot_min = minutes - 480

        else:
            reg_min = minutes
            ot_min = 0

        pay = (reg_min / 60) * rate + (ot_min / 60) * rate * 1.5

        return pay

class Receipt:
    def __init__(self, date, sale_amt):
        self.__date = date
        self.__sale_amt = float(sale_amt)

    def __str__(self):
        return 'The amount of $' + str(format(self.__sale_amt, ',.2f')) + ' was sold on ' + self.__date

class BankAccount:

    def __init__(self, bank_name, routing_number, account_id):
        self.__bank_name = bank_name
        self.__routing_number = routing_number
        self.__account_id = account_id
        self.__amount = 0

    def deposit(self, amt):
        self.__amount = float(amt)
        print ("I\'m depositing $", str(format(self.__amount, ',.2f')), "in ", self.__bank_name, " Account Number: ", self.__account_id, " using Routing Number: ", self.__routing_number)















