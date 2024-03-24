from django.db import models


class EmailSubscription(models.Model):
    email = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name
