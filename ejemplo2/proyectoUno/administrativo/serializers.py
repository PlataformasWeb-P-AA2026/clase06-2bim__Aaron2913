from django.contrib.auth.models import User, Group
from administrativo.models import Direccion, Estudiante, NumeroTelefonico
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EstudianteSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Estudiante
        fields = ['id', 'url', 'nombre', 'apellido', 'cedula', 'correo']


class NumeroTelefonicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NumeroTelefonico
        fields = '__all__'


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['id', 'descripcion', 'tipo', 'estudiante']