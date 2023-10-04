from django.db import models

class Thing():

    name = models.TextField
    description = models.TextField
    quantity = models.IntegerField

    def __init__(thing_name, thing_description, thing_quantity):
        name = thing_name
        description = thing_description
        quantity = thing_quantity