from fastapi import (FastAPI, Query)
from app.dto.OutputModel import OutputModel

app = FastAPI(title="Media")

@app.get('/media')
async def GetMedia(nota1: float = Query(gt=0), nota2: float = Query(gt=0)):
    media = (nota1 + nota2) / 2
    return OutputModel(media=media)