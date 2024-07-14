from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class PessoaDTO:
    id: Optional[int]
    nome: str
    data_nasc: date
    cpf: str
    sexo: str
    altura: float
    peso: float
