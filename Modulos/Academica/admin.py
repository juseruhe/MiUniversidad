from Modulos.Academica.models import Carrera, Curso, Estudiante, Matricula
from django.contrib import admin

# Register your models here.

admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Matricula)
