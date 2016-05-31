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