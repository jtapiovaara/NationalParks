from django.db import models


class NatParks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.ImageField(blank=True)
    location = models.URLField(blank=True)

    def __str__(self):
        """A string representation of the model."""
        return self.title
