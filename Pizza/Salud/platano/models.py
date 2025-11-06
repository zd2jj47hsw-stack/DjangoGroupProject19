from django.db import models
from django.db.models import Q
from django.db.models import UniqueConstraint
# Create your models here.

class Medico(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    especialidad = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(blank=True, null=True)

    class Meta:
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(fields=['rut'], name='unique_rut_medico')
        ]

    def __str__(self):
        return self.nombre_completo
    
class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField(max_length=10)
    sexo = models.CharField(max_length=1)
    telefono = models.CharField (blank=True, null=True)

    class Meta:
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(fields=['rut'], name='unique_rut_paciente')
        ]


    def __str__(self):
        return self.nombre_completo

class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField()
    hora_cita = models.TimeField()
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['fecha_cita', 'hora_cita']
        constraints = [
            models.UniqueConstraint(fields=['medico', 'fecha_cita', 'hora_cita'], name='unique_medico_cita'),
            models.UniqueConstraint(fields=['paciente', 'fecha_cita', 'hora_cita'], name='unique_paciente_cita')
        ]

    def __str__(self):
        return f"Cita de {self.paciente} con {self.medico} el {self.fecha_hora}"
    

    
    


    