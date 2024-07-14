from .models import Pessoa
from .serializers import PessoaSerializer
from rest_framework.exceptions import NotFound

class PessoaTask:
    @staticmethod
    def list_pessoas(nome=None):
        pessoas = Pessoa.objects.all()
        if nome:
            pessoas = pessoas.filter(nome_pessoa__icontains=nome)
        serializer = PessoaSerializer(pessoas, many=True)
        return serializer.data

    @staticmethod
    def create_pessoa(pessoa_data):
        serializer = PessoaSerializer(data=pessoa_data)
        if serializer.is_valid():
            pessoa = serializer.save()
            return serializer.data
        raise ValueError(serializer.errors)

    @staticmethod
    def get_pessoa(pk):
        try:
            pessoa = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            raise NotFound(f'Pessoa with id {pk} not found')
        serializer = PessoaSerializer(pessoa)
        return serializer.data

    @staticmethod
    def update_pessoa(pk, pessoa_data):
        try:
            pessoa = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            raise NotFound(f'Pessoa with id {pk} not found')
        serializer = PessoaSerializer(pessoa, data=pessoa_data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValueError(serializer.errors)

    @staticmethod
    def delete_pessoa(pk):
        try:
            pessoa = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            raise NotFound(f'Pessoa with id {pk} not found')
        pessoa.delete()

    @staticmethod
    def calcular_peso_ideal(altura, sexo):
        if sexo.upper() == 'M':
            peso_ideal = (72.7 * altura) - 58
        elif sexo.upper() == 'F':
            peso_ideal = (62.1 * altura) - 44.7
        else:
            raise ValueError("Sexo deve ser 'M' para masculino ou 'F' para feminino.")

        peso_ideal = round(peso_ideal, 2)
        return peso_ideal
