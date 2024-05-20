from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50, null = False)

    def __str__(self):
        return '{}'.format(self.name)




