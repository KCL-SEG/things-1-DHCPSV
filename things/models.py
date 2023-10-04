from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.TextField(default='', unique=True, blank=False, max_length=29)
    description = models.TextField(default='', max_length=119, blank=True)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])

    # def __init__(self, name, description, quantity):
    #     self.name = name
    #     self.description = description
    #     self.quantity = quantity