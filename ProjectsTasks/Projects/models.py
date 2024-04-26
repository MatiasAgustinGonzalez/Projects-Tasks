from django.db import models
from datetime import datetime

class Lider(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre}"


class Sponsor(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre}"


class Tarjeta(models.Model):
    class Tipo(models.TextChoices):
        planificado = 'Planificado', 'Planificado'
        en_curso = 'En Curso', 'En Curso'
        finalizado = 'Finalizado', 'Finalizado'

    lider = models.ForeignKey(Lider, on_delete=models.CASCADE,related_name='tarjetas')
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE,related_name='tarjetas')
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField(default=datetime.now)
    fecha_fin = models.DateField(default=datetime.now)
    estado = models.CharField(
        max_length=11,
        choices=Tipo.choices,
        default=Tipo.planificado,
    )

    def __str__(self):
        return f"Se cargó el Proyecto {self.titulo} para el Líder {self.lider}"

    def diferencia_mes(self):
        mes_tarjeta_fin = self.fecha_fin.month
        mes_tarjeta_inicio = self.fecha_inicio.month
        diferencia = mes_tarjeta_fin - mes_tarjeta_inicio
        return diferencia

    def diferencia_dias(self):
        mes_tarjeta_fin = self.fecha_fin.day
        mes_tarjeta_inicio = self.fecha_inicio.day
        diferencia = mes_tarjeta_fin - mes_tarjeta_inicio
        return diferencia