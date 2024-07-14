from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from .services import PessoaService
from .dto import PessoaDTO

class PessoaController(APIView):
    def get(self, request):
        nome = request.query_params.get('nome', None)
        pessoas = PessoaService.list_pessoas(nome)
        return Response([pessoa.__dict__ for pessoa in pessoas])

    def post(self, request):
        try:
            pessoa_dto = PessoaService.create_pessoa(request.data)
            return Response(pessoa_dto.__dict__, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

class PessoaDetailController(APIView):
    def get(self, request, pk):
        try:
            pessoa_dto = PessoaService.get_pessoa(pk)
            return Response(pessoa_dto.__dict__)
        except NotFound as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            pessoa_dto = PessoaService.update_pessoa(pk, request.data)
            return Response(pessoa_dto.__dict__)
        except ValueError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except NotFound as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            PessoaService.delete_pessoa(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotFound as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

class PesoIdealController(APIView):
    def post(self, request):
        try:
            altura = request.data.get('altura')
            sexo = request.data.get('sexo')
            if not altura or not sexo:
                return Response('Altura e sexo são obrigatórios', status=status.HTTP_400_BAD_REQUEST)

            peso_ideal = PessoaService.calcular_peso_ideal(altura, sexo)
            return Response({'peso_ideal': peso_ideal}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
