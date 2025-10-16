from django.db import models
from django.urls import reverse


ACTIVITIES = (
        ('H', 'Hiking'),
        ('C', 'Camping'),
        ('S', 'Sight-seeing'),
        ('W', 'Swimming')
)

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

class Log(models.Model):
        date = models.DateField('Travelers Log')
        activity = models.CharField(
                max_length=1,
                choices = ACTIVITIES,
                default=ACTIVITIES[0][0]
                )
        
        park = models.ForeignKey(Park, on_delete=models.CASCADE)

        def __str__(self):
                return f"I went {self.get_activity_display()} on {self.date}"
        
        class Meta:
                ordering = ['-date']