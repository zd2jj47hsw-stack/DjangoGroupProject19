from django import forms
from .models import Medico, Paciente, Cita

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre_completo', 'rut', 'especialidad', 'correo', 'telefono']

#Correo debe ser unico, constraint? o validacion en el form? o ambas?
#validacion de rut
#listar registrar editar eliminar medicos y pacientes

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre_completo', 'rut', 'fecha_nacimiento', 'sexo', 'telefono']

#listar registrar editar eliminar medicos y pacientes
#validacion de rut
#dejamos que los pacientes no tengan correo unico por si acaso

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['medico', 'paciente', 'especialidad', 'fecha_cita', 'hora_cita', 'observaciones']
        
#Registrar, modificar, buscar y eliminar citas.
#Validar que no existan conflictos de horario ni duplicidad de citas por paciente o médico.
#Filtrar citas por fecha, médico o paciente mediante formularios GET.