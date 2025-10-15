from django.db import models
from django.urls import reverse

class Park(models.Model):
        name = models.CharField(max_length=100)
        state = models.CharField(max_length=20)
        description = models.TextField(max_length = 250)
        rating = models.IntegerField()

        def __str__(self):
                return self.name
        #redirect on successful create
        def get_absolute_url(self):
                return reverse('park-detail', kwargs={'park_id': self.id})

