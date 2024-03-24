from django.db import models
from courses.models import Course


class Student(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE,)
    fullname = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=True)
    phone = models.IntegerField(blank=True, help_text='Phone Number')

    def __str__(self):
        return self.fullname