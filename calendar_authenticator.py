from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class CalendarAuthenticator:
    API_SERVICE_NAME = 'calendar'
    API_VERSION = 'v3'
    HOST = 'localhost'
    PORT = 8080

    @staticmethod
    def get_calendar_service(client_secret_file, scopes, auth_prompt_message, success_message):
        flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
        credentials = flow.run_local_server(
            host = CalendarAuthenticator.HOST,
            port = CalendarAuthenticator.PORT,
            authorization_prompt_message = auth_prompt_message,
            success_message = success_message,
            open_browser = True
        )

        return build(CalendarAuthenticator.API_SERVICE_NAME, CalendarAuthenticator.API_VERSION, credentials=credentials)