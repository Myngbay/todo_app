from django.db import models


class Todo:
    def __init__(self, task_id, user_name, title, text, datetime, done):
        self.task_id = task_id
        self.user_name = user_name
        self.title = title
        self.text = text
        self.datetime = datetime
        self.done = done