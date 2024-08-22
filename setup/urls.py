from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante, ListaMatriculaCurso

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudante')
router.register('cursos', CursoViewSet, basename='Curso')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudante.as_view()),
    path('curso/<int:pk>/matriculas/', ListaMatriculaCurso.as_view()),
]
