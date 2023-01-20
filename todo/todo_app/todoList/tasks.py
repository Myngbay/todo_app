from todo_app.celery import app
from django.core.mail import send_mail
from .models import Todo


@app.task
def mail_created(task_id):
    """
    Задача для отправки уведомления по электронной почте.
    """
    task = Todo.objects.get(id=task_id)
    subject = 'Задача. {}'.format(task_id)
    message = 'Dear {},\n\nYour task has been successfully added to To Do.\
                Your task id is {}.'.format(task.first_name,
                                             task.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@todo_app.com',
                          [task.email])
    return mail_sent