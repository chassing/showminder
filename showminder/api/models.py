
from django.db import models


class ApiNotification(models.Model):

    subject = models.CharField(max_length=255)
    message = models.TextField()
    when = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-when", "subject"]

    def __str__(self):
        return self.subject

    @classmethod
    def add_message(cls, subject, message):
        cls.objects.create(subject=subject, message=message)
