from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=1000, blank=True)
    sessions = models.IntegerField(blank=False, help_text='Number of sessions')
    session_duration = models.IntegerField(blank=False, help_text='Session duration in minutes')
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    tags = models.CharField(max_length=1000, blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_hidden = models.BooleanField(default=False)
    image_url = models.CharField(max_length=1000, blank=True)
    max_students = models.IntegerField(blank=False, default=3)

    def __str__(self):
        return self.name