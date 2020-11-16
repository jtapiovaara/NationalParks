from django.db import models
import requests


class NatParks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.ImageField(blank=True)
    location = models.URLField(blank=True)

    def __str__(self):
        """A string representation of the model."""
        return self.title


class NatParkGeo(models.Model):
    title = models.ForeignKey(NatParks, on_delete=models.CASCADE)
    postcode = models.IntegerField(blank=True, default=99999)
    calltitle = models.CharField(max_length=200)
    place = models.CharField(blank=True, max_length=128, default='paikka')
    state = models.CharField(blank=True, max_length=128, default='osav')
    kohdeLat = models.DecimalField(max_digits=10, decimal_places=8, default=64.12)
    kohdeLon = models.DecimalField(max_digits=12, decimal_places=8, default=-108.12)

    # def __str__(self):
    #     """A string representation of the model."""
    #     return self.calltitle

    def __str__(self):
        return str(self.postcode).zfill(5)

    def save(self, *args, **kwargs):
        kysely = requests.get(f'https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude'
                              f'-and-longitude&q={self.postcode}&facet=state&facet=timezone&facet=dst')
        self.place = kysely.json()['records'][0]['fields']['city']
        self.state = kysely.json()['records'][0]['fields']['state']
        self.kohdeLat = kysely.json()['records'][0]['fields']['latitude']
        self.kohdeLon = kysely.json()['records'][0]['fields']['longitude']
        super().save(*args, **kwargs)
