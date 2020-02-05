from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=100)
    provider = models.CharField(max_length=50, null=True)
    link = models.URLField()
    movie = models.BooleanField(default=False)

    def __str__(self):
        return self.name
