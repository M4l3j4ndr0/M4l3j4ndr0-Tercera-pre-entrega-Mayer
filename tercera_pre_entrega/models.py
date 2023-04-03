from django.db import models

class Post (models.Model):
    carousel_caption_title = models.CharField(max_length=30)
    carousel_caption_description = models.CharField(max_length=80)
    heading  = models.CharField(max_length=15)
    description = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.id} - {self.heading}"

class Notas(models.Model):
    alumno = models.TextField(max_length=100)
    materia = models.TextField(max_length=100)
    fecha_parcial = models.DateTimeField(auto_now_add=True)
    nota_parcial = models.TextField(max_length=2)

    def __str__(self):
        return f"parcial numero: {self.id}   --   Alumno: {self.alumno}   --   fecha de parcial {self.fecha_parcial}  --   nota de parcial {self.nota_parcial}"


class Usuario(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"id usuario: {self.id} - nombre usuario: {self.nombre} - apellido usuario {self.apellido} - fecha nacimiento {self.fecha_nacimiento}"