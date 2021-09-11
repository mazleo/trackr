from calendar_utility import CalendarUtility

class CalendarEventListImporter:
    @staticmethod
    def import_task_events(task_events, service):
        calendar_id = CalendarUtility.get_calendar_id(service)
        calendar_timezone = CalendarUtility.get_calendar_timezone(service)

        for task_event in task_events:
            calendar_event = {
                'summary': task_event.summary,
                'description': task_event.description,
                'start': {
                    'dateTime': task_event.start_time,
                    'timeZone': calendar_timezone
                },
                'end': {
                    'dateTime': task_event.end_time,
                    'timeZone': calendar_timezone
                },
                'colorId': task_event.color_id
            }

            event_response = service.events().insert(calendarId = calendar_id, body = calendar_event).execute()
            print(f'{task_event.summary} event created: {event_response.get("htmlLink")}')