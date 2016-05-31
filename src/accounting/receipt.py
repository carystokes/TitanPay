class Receipt:
    def __init__(self, date, sale_amt):
        self.__date = date
        self.__sale_amt = float(sale_amt)

    def __str__(self):
        return 'The amount of $' + str(format(self.__sale_amt, ',.2f')) + ' was sold on ' + self.__date