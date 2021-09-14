import os.path

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

class CalendarAuthenticator:
    API_SERVICE_NAME = 'calendar'
    API_VERSION = 'v3'
    HOST = 'localhost'
    PORT = 8080

    @staticmethod
    def get_calendar_service(client_secret_file, token_file, scopes, auth_prompt_message, success_message):
        credentials = None
        if os.path.exists(token_file):
            credentials = Credentials.from_authorized_user_file(token_file, scopes)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
                credentials = flow.run_local_server(
                    host = CalendarAuthenticator.HOST,
                    port = CalendarAuthenticator.PORT,
                    authorization_prompt_message = auth_prompt_message,
                    success_message = success_message,
                    open_browser = True
                )
            with open(token_file, 'w') as token:
                token.write(credentials.to_json())

        return build(CalendarAuthenticator.API_SERVICE_NAME, CalendarAuthenticator.API_VERSION, credentials=credentials)