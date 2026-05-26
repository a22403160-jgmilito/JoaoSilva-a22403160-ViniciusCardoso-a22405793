from ninja import NinjaAPI 
from .models import Autor
api = NinjaAPI(
    title = "api Restful Biblioteca"

)


@api.get("ola/")
def ola(request):
    return {"mensagem": "ola!"}

@api.get("autores1/")
def autores1(request):
    autores = [{'nome': a.nome, 'ano_nascimento': a.ano_nascimento} for a in Autor.objects.all()]
    return autores

from .schemas import AutorOut, ErrorSchema, AutorIn
from typing import List
@api.get(
    "autores/",
    response= {200: List[AutorOut]},
    tags = ['Autores']
)
def autores(request):
    return 200, Autor.objects.all()

@api.get("autores/{autor_id}",
    response = {200: AutorOut, 404: ErrorSchema}
)
def autor(request, autor_id):

    try:
        return 200, Autor.objects.get(id = autor_id)
    except: 
        return 404, {"message": "Autor nao encontrado"}

@api.get("autores/autorLivro/{autor_id}",
    response = {200: AutorOut, 404: ErrorSchema}
)
def autorLivros(request, autor_id):

    try:
        return 200, Autor.objects.get(id = autor_id).select_related("livros")
    except: 
        return 404, {"message": "Autor nao encontrado"}

@api.post(
    "autores/",
    response = {201: AutorOut},
    tags=["Autores"]
)
def cria_autor(request, data: AutorIn):
    autor.objects.create(**data.dict())
    return 201, autor 