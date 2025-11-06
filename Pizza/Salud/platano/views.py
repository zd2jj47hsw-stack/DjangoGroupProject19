from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Medico, Paciente, Cita
from .forms import MedicoForm, PacienteForm, CitaForm
# Create your views here.
