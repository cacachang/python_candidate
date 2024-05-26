from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Candidate(models.Model):
  name = models.CharField(max_length=100)
  party = models.CharField(max_length=50)
  age = models.IntegerField(
    validators=[
            MaxValueValidator(100),
            MinValueValidator(40)
        ]
  )