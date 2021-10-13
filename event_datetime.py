class EventDateTime:
    def __init__(self, date, start_time, end_time):
        date_values = self.extract_date_values(date)
        start_time_values = self.extract_time_values(start_time)
        end_time_values = self.extract_time_values(end_time)

        self.year = int(date_values[0])
        self.month = int(date_values[1])
        self.day = int(date_values[2])

        self.start_hour = int(start_time_values[0])
        self.start_minute = int(start_time_values[1])
        self.start_second = int(start_time_values[2])

        self.end_hour = int(end_time_values[0])
        self.end_minute = int(end_time_values[1])
        self.end_second = int(end_time_values[2])

        if self.start_hour < 4:
            self.day += 1

        self.fix_passed_time()

    def __str__(self):
        return f'{str(self.year)}-{str(self.month)}-{str(self.day)} {str(self.start_hour)}:{str(self.start_minute)}:{str(self.start_second)}.{str(self.start_millisecond)}-{str(self.end_hour)}:{str(self.end_minute)}:{str(self.end_second)}.{str(self.end_millisecond)}'

    def fix_passed_time(self):
        if self.is_passed_end_year():
            self.year += 1
            self.month = 1
            self.day = 1
        elif self.is_passed_end_month():
            self.month += 1
            self.day = 1

    def is_passed_end_year(self):
        return self.month == 12 and self.day > 31

    def is_passed_end_month(self):
        month = self.month
        day = self.day

        thirtyone_day_months = [1, 3, 5, 7, 8, 10, 12]
        thirty_day_months = [4, 6, 9, 11]

        is_feb = month == 2
        is_thirtyone_day_month = month in thirtyone_day_months
        is_thirty_day_month = month in thirty_day_months

        is_passed_end_month = (is_feb and day > 28) or (is_thirtyone_day_month and day > 31) or (is_thirty_day_month and day > 30)

        return is_passed_end_month

    def extract_date_values(self, date):
        return date.split('-')

    def extract_time_values(self, time):
        time_values = []

        values = time.split(':')

        time_values.append(values[0])
        time_values.append(values[1])

        seconds = values[2].split('.')

        time_values.append(seconds[0])

        return time_values