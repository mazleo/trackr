import task_event

import sys
import csv
import datetime
import time

class TimesheetParser:

    @staticmethod
    def parse_csv_file_to_task_events(csv_filename):
        with open(csv_filename, newline='') as csv_file:
            timesheet_reader = csv.reader(csv_file, delimiter=',', quotechar='"')

            TimesheetParser.extract_csv_contents(timesheet_reader)
    
    @staticmethod
    def extract_csv_contents(timesheet_reader):
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