from .models import Project
from rest_framework import viewsets, permissions
from .secuencia import ProjectSecuencia

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    secuencia_class = ProjectSecuencia

