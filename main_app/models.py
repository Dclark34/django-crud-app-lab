from django.db import models

class Park(models.Model):
        name = models.CharField(max_length=100)
        state = models.CharField(max_length=20)
        description = models.TextField(max_length = 250)
        rating = models.IntegerField()

        def __str__(self):
                return self.name
