from calendar_utility import CalendarUtility
import json

class CalendarColor:
    TASK_COLORS_FILE = 'task_colors.json'

    @staticmethod
    def insert_color_calendar(service):
        calendar_id = CalendarUtility.get_calendar_id(service)

        with open(CalendarColor.TASK_COLORS_FILE, mode = 'r') as task_colors_file:
            json_string = task_colors_file.read()

            task_colors_wrapper = json.JSONDecoder().decode(json_string)

            body = {
                'id': calendar_id,
                'backgroundColor': task_colors_wrapper.get('calendar').get('background'),
                'foregroundColor': task_colors_wrapper.get('calendar').get('foreground')
            }

            service.calendarList().insert(body = body, colorRgbFormat = True).execute()

    @staticmethod
    def get_match_color_id(project, task):
        with open(CalendarColor.TASK_COLORS_FILE, mode = 'r') as task_colors_file:
            json_string = task_colors_file.read()

            task_colors_wrapper = json.JSONDecoder().decode(json_string)

            if CalendarColor.is_task_meeting(project, task):
                return task_colors_wrapper.get('tasks').get('meetings')

            if CalendarColor.is_runbits_task(project, task_colors_wrapper):
                return task_colors_wrapper.get('projects').get('runbits').get('color_id')

            project_lower = project.lower()
            return task_colors_wrapper.get('projects').get(project_lower)

    @staticmethod
    def is_task_meeting(project, task):
        task_lower = task.lower()
        return (project == 'JO-5 General Work') and ('meeting' in task_lower) and ('summarize' not in task_lower)

    @staticmethod
    def is_runbits_task(project, task_colors_wrapper):
        if project in task_colors_wrapper.get('projects').get('runbits').get('project_names'):
            return True
        return False