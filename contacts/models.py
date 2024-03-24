from django.db import models


class Contact(models.Model):
    fullname = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=True)
    phone = models.IntegerField(blank=True, help_text='Phone Number')
    query = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.fullname