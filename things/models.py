from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.TextField(max_length=30, default='', unique=True, blank=False)
    description = models.TextField(max_length=120, default='', blank=True)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    # def __init__(self, name, description, quantity):
    #     self.name = name
    #     self.description = description
    #     self.quantity = quantity