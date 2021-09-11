from calendar_utility import CalendarUtility

class CalendarColor:
    PROJECT_TRACKR_COLOR_ID = 4;
    PROJECT_BOOKS_COLOR_ID = 3;
    PROJECT_RUITS_COLOR_ID = 5;
    PROJECT_PRODUCTIVITY_COLOR_ID = 1;
    TASK_MEETING_COLOR_ID = 11;

    @staticmethod
    def insert_color_calendar(service, hex_bg_color, hex_fg_color):
        calendar_id = CalendarUtility.get_calendar_id(service)

        body = {
            'id': calendar_id,
            'backgroundColor': hex_bg_color,
            'foregroundColor': hex_fg_color
        }

        service.calendarList().insert(body = body, colorRgbFormat = True).execute()

    @staticmethod
    def get_match_color_id(project, task):
        if 'meeting' in task.lower():
            return CalendarColor.TASK_MEETING_COLOR_ID;
        
        projectl = project.lower()
        is_work_project = ('client projects' in projectl) or ('study spaces' in projectl) or ('general work' in projectl)

        if is_work_project:
            return CalendarColor.PROJECT_RUITS_COLOR_ID

        if 'trackr' in projectl:
            return CalendarColor.PROJECT_TRACKR_COLOR_ID
        elif 'books' in projectl:
            return CalendarColor.PROJECT_BOOKS_COLOR_ID
        elif 'productivity' in projectl:
            return CalendarColor.PROJECT_PRODUCTIVITY_COLOR_ID