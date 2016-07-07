class TimeCard:

    def __init__(self, date: object, st_time: object, end_time: object) -> object:
        self.__date = date
        self.__start_time = st_time
        self.end_time = end_time

    def get_tcdate(self):
        return self.__date

    def calculate_daily_pay(self, rate_str):
        rate = float(rate_str)
        end_minutes = (int(self.end_time) // 100) * 60 + (int(self.end_time) - (int(self.end_time) // 100)*100)
        start_minutes = (int(self.__start_time) // 100) * 60 + (int(self.__start_time) - (int(self.__start_time) // 100)*100)

        minutes = end_minutes - start_minutes

        if minutes > 480:
            reg_min = 480
            ot_min = minutes - 480

        else:
            reg_min = minutes
            ot_min = 0

        pay = (reg_min / 60) * rate + (ot_min / 60) * rate * 1.5

        return pay

    def set_end_time(self, end_time):
        self.end_time = end_time
