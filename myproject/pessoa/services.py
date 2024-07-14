from .tasks import PessoaTask
from .dto import PessoaDTO
from typing import List

class PessoaService:
    @staticmethod
    def list_pessoas(nome: str = None) -> List[PessoaDTO]:
        pessoas_data = PessoaTask.list_pessoas(nome)
        return [PessoaDTO(**data) for data in pessoas_data]

    @staticmethod
    def create_pessoa(pessoa_data: dict) -> PessoaDTO:
        data = PessoaTask.create_pessoa(pessoa_data)
        return PessoaDTO(**data)

    @staticmethod
    def get_pessoa(pk: int) -> PessoaDTO:
        data = PessoaTask.get_pessoa(pk)
        return PessoaDTO(**data)

    @staticmethod
    def update_pessoa(pk: int, pessoa_data: dict) -> PessoaDTO:
        data = PessoaTask.update_pessoa(pk, pessoa_data)
        return PessoaDTO(**data)

    @staticmethod
    def delete_pessoa(pk: int) -> None:
        PessoaTask.delete_pessoa(pk)

    @staticmethod
    def calcular_peso_ideal(altura: float, sexo: str) -> float:
        return PessoaTask.calcular_peso_ideal(altura, sexo)
