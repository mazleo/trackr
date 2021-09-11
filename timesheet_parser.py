from task_event import TaskEvent
from event_datetime import EventDateTime
from calendar_color import CalendarColor

import csv
import datetime

class TimesheetParser:
    @staticmethod
    def parse_csv_file_to_task_events(csv_filename):
        with open(csv_filename, newline='') as csv_file:
            timesheet_reader = csv.reader(csv_file, delimiter=',', quotechar='"')

            return TimesheetParser.extract_csv_contents(timesheet_reader)
    
    @staticmethod
    def extract_csv_contents(timesheet_reader):
        task_events = []

        row_count = 0
        for row in timesheet_reader:
            row_count += 1
            if row_count == 1:
                continue
            
            date = row[0]
            start_time = row[1]
            end_time = row[2]
            project = row[3]
            task = row[4]
            comment = row[6]

            task_event_color_id = CalendarColor.get_match_color_id(project, task)

            task_event_summary = TimesheetParser.format_summary(project, task)
            task_event_description = comment.strip()

            start_end_ical = TimesheetParser.format_event_datetime_to_ical(date, start_time, end_time)
            task_event_start_time = start_end_ical[0]
            task_event_end_time = start_end_ical[1]

            task_events.append(TaskEvent(task_event_summary, task_event_description, task_event_start_time, task_event_end_time, task_event_color_id))

        return task_events

    @staticmethod
    def format_summary(project, task):
        return project + ' | ' + task.replace('General | ', '')

    @staticmethod
    def format_event_datetime_to_ical(date, start_time, end_time):
        event_datetime = EventDateTime(date, start_time, end_time)

        start_datetime = datetime.datetime(event_datetime.year, event_datetime.month, event_datetime.day, hour=event_datetime.start_hour, minute=event_datetime.start_minute, second=event_datetime.start_second)
        end_datetime = datetime.datetime(event_datetime.year, event_datetime.month, event_datetime.day, hour=event_datetime.end_hour, minute=event_datetime.end_minute, second=event_datetime.end_second)

        return [start_datetime.isoformat(), end_datetime.isoformat()]