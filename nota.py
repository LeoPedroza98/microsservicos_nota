
import datetime
from enum import Enum
from typing import List

from uuid import UUID, uuid4

from pydantic import BaseModel

    
class Nota(BaseModel):
    atividade_id: int
    disciplina_id: int
    aluno_id : int
    nota : int    
    
    
ATIVIDADE = {}


def post_nota(atividade_id:int,disciplina_id:int,nota:str):
    nota = Nota(
        atividade_id= atividade_id,
        nota=nota,
        disciplina_id= disciplina_id
    )
    ATIVIDADE[str(nota.atividade_id)] = nota
    return nota


def get_atividade(atividad_id: str):
    return ATIVIDADE.get(atividad_id)