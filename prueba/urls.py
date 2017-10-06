"""cotizador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
# ======= PARA EL EJEMPLO
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
# ======= PARA EL API
from autosegcotizador import views
from autosegcotizador.views import *


# =======================EJEMPLO DE USUARIOS=============
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# Routers provide an easy way of automatically determining the URL conf.


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'marca', MarcaViewSet)
router.register(r'modelo', ModeloViewSet)
router.register(r'version', VersionViewSet)
router.register(r'danios', DaniosMaterialesViewSet)
router.register(r'derecho-membresia', DerechoMembresiaViewSet)

# =======================TERMINA EJEMPLO DE USUARIOS=============


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^marca/', MarcaViewSet.as_view({'get': 'list'})),
    url(r'^modelo/', ModeloViewSet.as_view({'get': 'list'})),
    url(r'^version/', VersionViewSet.as_view({'get': 'list'})),
    url(r'^suma-variables/', suma_variables),
    url(r'^danios/', DaniosMaterialesViewSet.as_view({'get': 'list'})),
    url(r'^derecho-membresia/', DerechoMembresiaViewSet.as_view({'get': 'list'})),
]
