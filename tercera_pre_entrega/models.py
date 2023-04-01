from django.db import models

class Tarea(models.Model):
    nombre = models.TextField(max_length=100)
