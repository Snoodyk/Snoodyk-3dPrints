from django.db import models


class about(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=99999)

    def __str__(self):
        return self.title