class CalendarUtility:
    CALENDAR_NAME = 'trackr'
    CALENDAR_DESCRIPTION = 'A more accurate history of tasks. trackr imports timeBro timesheet CSV exports for more accurate time tracking.'
    CALENDAR_TIMEZONE = 'UTC'

    @staticmethod
    def get_calendar_id(service):
        calendar_list = CalendarUtility.get_list_calendars(service)

        for calendar_entry in calendar_list:
            if calendar_entry.get('summary') == CalendarUtility.CALENDAR_NAME:
                return calendar_entry.get('id')

    @staticmethod
    def get_calendar_timezone(service):
        calendar_list = CalendarUtility.get_list_calendars(service)

        for calendar_entry in calendar_list:
            if calendar_entry.get('summary') == CalendarUtility.CALENDAR_NAME:
                return calendar_entry.get('timeZone')

    @staticmethod
    def get_list_calendars(service):
        calendar_list = []

        page_token = None
        while True:
            calendar_dict = service.calendarList().list(pageToken=page_token).execute()

            calendar_list.extend(calendar_dict['items'])

            page_token = calendar_dict.get('nextPageToken')

            if page_token == None:
                break

        return calendar_list