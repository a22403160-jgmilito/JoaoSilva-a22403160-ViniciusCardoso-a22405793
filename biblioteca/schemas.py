from ninja import Schema


class AutorIn(Schema):
    nome: str 
    ano_nascimento : int
    nacionalidade: str
    retrato : str

class AutorOut(Schema):
    id : int
    nome: str 
    ano_nascimento : int
    retrato : str

class ErrorSchema(Schema):
    message: str
class Livro(Schema):
    id: int
    title: str
from typing import List
class AutorComLivrosOut(AutorOut):
    livros : List[AutorOut]