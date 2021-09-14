import sys

from file_utility import FileUtility
from timesheet_parser import TimesheetParser

from calendar_authenticator import CalendarAuthenticator
from calendar_utility import CalendarUtility
from calendar_generator import CalendarGenerator
from calendar_color import CalendarColor
from calendar_event_list_importer import CalendarEventListImporter

CLIENT_SECRET_FILE = sys.argv[1]
TOKEN_FILE = 'token.json'
API_SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/calendar.events'
]
API_AUTH_PROMPT_MESSAGE = 'Please give the Calendar and Events permissions.'
API_SUCCESS_MESSAGE = 'Calendar and Events permissions successfully granted.'

calendar_service = CalendarAuthenticator.get_calendar_service(CLIENT_SECRET_FILE, TOKEN_FILE, API_SCOPES, API_AUTH_PROMPT_MESSAGE, API_SUCCESS_MESSAGE)

file_names = FileUtility.extract_file_names(sys.argv)

for file_name in file_names:
    task_events = TimesheetParser.parse_csv_file_to_task_events(file_name)

    CalendarGenerator.generate_trackr_calendar_if_not_exists(calendar_service)

    CalendarColor.insert_color_calendar(calendar_service)

    CalendarEventListImporter.import_task_events(task_events, calendar_service)