from rest_framework import serializers
from .models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):

    nome = serializers.CharField(source='nome_pessoa')
    data_nasc = serializers.DateField(source='data_nasc_pessoa')
    cpf = serializers.CharField(source='cpf_pessoa')
    sexo = serializers.CharField(source='sexo_pessoa')
    altura = serializers.FloatField(source='altura_pessoa')
    peso = serializers.FloatField(source='peso_pessoa')

    class Meta:
        model = Pessoa
        fields = ['id','nome', 'data_nasc', 'cpf', 'sexo', 'altura', 'peso']
