from django.db import models

class Thing(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')
    quantity = models.IntegerField(default=0)

    # def __init__(self, name, description, quantity):
    #     self.name = name
    #     self.description = description
    #     self.quantity = quantity