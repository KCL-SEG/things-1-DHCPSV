from django.db import models

class Thing(models.Model):
    name = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()

    # def __init__(self, name, description, quantity):
    #     self.name = name
    #     self.description = description
    #     self.quantity = quantity