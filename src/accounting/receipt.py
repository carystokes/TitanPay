class Receipt:
    def __init__(self, emp_id, lname, item, units, unit_cost, total_amt):
        self.__emp_id = emp_id
        self.__lname = lname
        self.__item = item
        self.__units = units
        self.__unit_cost = unit_cost
        self.__total_amt = total_amt

    def get_pay_data(self):
        return self.__total_amt