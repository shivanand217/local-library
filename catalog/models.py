from django.db import models

# Create your models here.

class Genre(models.Model):

    name = models.CharField(max_length=200,help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        # string for representing the model object
        return self.name

        