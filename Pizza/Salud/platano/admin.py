from django.contrib import admin
from .models import Medico, Paciente, Cita
# Register your models here.

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_completo", "rut", "especialidad", "correo", "telefono",)
    list_filter = ()
    search_fields = ()
    
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_completo", "rut", "fecha_nacimiento","sexo", "telefono")
    list_filter = ()
    search_fields = ()

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ("id", "medico", "paciente", "especialidad", "fecha_cita", "hora_cita","observaciones")
    list_filter = ()
    search_fields = ()
