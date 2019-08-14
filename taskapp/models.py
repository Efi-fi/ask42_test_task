from django.contrib.postgres.fields import JSONField
from django.db import models


class Data(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    data = JSONField()

    def __str__(self):
        return str(self.datetime)

