class TaskEvent:
    def __init__(self, summary, description, start_time, end_time):
        self.summary = summary
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
    
    def __str__(self):
        return f"'summary': '{self.summary}',\n'description': '{self.description}',\n'start': {{\n\t'dateTime': '{self.start_time}'\n}},\n'end': {{\n\t'dateTime': '{self.end_time}'\n}}"