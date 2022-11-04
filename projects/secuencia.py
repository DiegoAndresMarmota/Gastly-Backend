from rest_framework import secuencia
from .models import project


class ProjectSecuencia(secuencia.ModelSecuencia):
    class Meta:
        model = project
        fields = ('id', 'titulo', 'descripcion',
                  'detalles', 'stock', 'precios')
        read_only_fields = ('detalles')
