from django.db import models
from django.urls import reverse
import uuid


# Create your models here.

class Pressure(models.Model):
    objects = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for pressure')
    pressure = models.CharField(max_length=6)
    date_of_create = models.DateField('Create time', auto_now=True)
    date_of_update = models.DateField('Update time', auto_now=True)

    class Meta:
        ordering = ['pressure', 'date_of_create']

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.pressure}'
