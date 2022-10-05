import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from typing import List

from . import nota

app = FastAPI()


class submissao_nota(BaseModel):
    atividade_id: int
    disciplina_id: int
    nota : int


@app.get('/')
async def index():

    return {"DEU BOM": "OK"}


@app.post("/nota", response_model=nota.Nota)
async def nota_correction(nota_req: submissao_nota):
    notas = nota.nota_correction(**nota_req.dict())

    return notas


@app.get("/atividade/{atividade_id}", response_model=nota.Nota)
async def get_atividadeSemNotas(atividade_id: str):
    print(nota.ATIVIDADE)
    atividades = nota.get_atividade(atividade_id=atividade_id)

    if atividades is None:
        raise HTTPException(
            status_code=404,
            detail="Atividade não encontrada"
        )

    return atividades