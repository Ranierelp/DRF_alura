from django.contrib import admin
from escola.models import Estudante, Curso


class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email','cpf','data_nascimento', 'celular')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
    
admin.site.register(Estudante, Estudantes)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao')
    list_display_links = ('id', 'codigo')
    search_fields = ('codigo',)

admin.site.register(Curso, Cursos)