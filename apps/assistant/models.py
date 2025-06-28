from django.db import models
from apps.users.models import User

class RefAssistant(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    assistant_sms = models.TextField()
    date_assistant = models.DateField()
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'assistant'
        verbose_name = 'Напоминание'
        verbose_name_plural = 'Напоминания'

    def __str__(self):
        return f"{self.assistant_sms} — {'Сделано' if self.is_done else 'Запланировано'}"