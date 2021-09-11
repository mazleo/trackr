import sys

from timesheet_parser import TimesheetParser

from calendar_authenticator import CalendarAuthenticator
from calendar_utility import CalendarUtility
from calendar_generator import CalendarGenerator
from calendar_event_list_importer import CalendarEventListImporter

CLIENT_SECRET_FILE = sys.argv[1]
API_SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/calendar.events'
]
API_AUTH_PROMPT_MESSAGE = 'Please give the Calendar and Events permissions.'
API_SUCCESS_MESSAGE = 'Calendar and Events permissions successfully granted.'

task_events = TimesheetParser.parse_csv_file_to_task_events(sys.argv[2])

calendar_service = CalendarAuthenticator.get_calendar_service(CLIENT_SECRET_FILE, API_SCOPES, API_AUTH_PROMPT_MESSAGE, API_SUCCESS_MESSAGE)

CalendarGenerator.generate_trackr_calendar_if_not_exists(calendar_service)

CalendarEventListImporter.import_task_events(task_events, calendar_service)