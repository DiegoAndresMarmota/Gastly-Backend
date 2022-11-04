from rest_framework import secuencia
from .models import Project


class ProjectSecuencia(secuencia.ModelSecuencia):
    class Meta:
        model = Project
        fields = ('id', 'titulo', 'descripcion',
                  'detalles', 'stock', 'precios')
        read_only_fields = ('detalles', )
