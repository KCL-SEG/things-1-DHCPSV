from django.db import models

class Thing():
    
    name = models.TextField
    description = models.TextField
    quantity = models.IntegerField

    def __init__(name, description, quantity):
        name = name
        description = description
        quantity = quantity