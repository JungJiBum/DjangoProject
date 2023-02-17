from django.db import models

# Create your models here.


class webtoonData(models.Model):
    title = models.CharField(max_length=50)
    title_numbers = models.IntegerField(default=0)
    week = models.CharField(max_length=10, null=True, default='')

    def __str__(self):
        return self.title
