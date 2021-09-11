from calendar_utility import CalendarUtility

class CalendarGenerator:

    @staticmethod
    def generate_trackr_calendar_if_not_exists(service):
        exists = CalendarGenerator.check_trackr_exists(service)

        if not exists:
            calendar_entry = {
                'summary': CalendarUtility.CALENDAR_NAME,
                'description': CalendarUtility.CALENDAR_DESCRIPTION
            }

            service.calendars().insert(body=calendar_entry).execute()
            print('Calendar ' + CalendarUtility.CALENDAR_NAME + ' created.')
        else:
            print('Calendar ' + CalendarUtility.CALENDAR_NAME + ' already exists. Not created.')

    @staticmethod
    def check_trackr_exists(service):
        calendar_list = CalendarUtility.get_list_calendars(service)

        calendar_exists = False
        for calendar_entry in calendar_list:
            if calendar_entry.get('summary') == CalendarUtility.CALENDAR_NAME:
                calendar_exists = True
                return calendar_exists

        return calendar_exists