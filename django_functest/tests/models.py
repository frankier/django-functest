from django.db import models


# After making changes here, run:
#   ./runtests.py --update-migration
class Thing(models.Model):
    ELEMENT_EARTH = 'e'
    ELEMENT_WATER = 'w'
    ELEMENT_AIR = 'a'
    ELEMENT_FIRE = 'f'
    ELEMENT_CHOICES = [
        (ELEMENT_EARTH, 'Earth'),
        (ELEMENT_WATER, 'Water'),
        (ELEMENT_AIR, 'Air'),
        (ELEMENT_FIRE, 'Fire')
    ]

    name = models.CharField(max_length=255)
    big = models.BooleanField(default=False)
    clever = models.BooleanField(default=False)
    element_type = models.CharField(max_length=1,
                                    choices=ELEMENT_CHOICES)
    count = models.IntegerField(default=0)
    description = models.TextField(blank=True)
