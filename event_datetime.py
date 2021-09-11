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

    def __str__(self):
        return f'{str(self.year)}-{str(self.month)}-{str(self.day)} {str(self.start_hour)}:{str(self.start_minute)}:{str(self.start_second)}.{str(self.start_millisecond)}-{str(self.end_hour)}:{str(self.end_minute)}:{str(self.end_second)}.{str(self.end_millisecond)}'

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