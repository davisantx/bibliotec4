from core.autores import montar_autor
from ui.tabela import formatar_tabela
from data.db import buscar, buscar_todos, excluir, listar, salvar


def montar_livro(titulo: str, nome_autor: str, status: str) -> dict | None:
    if len(titulo.replace(" ", "")) < 1:
        print("Título muito curto!")
        return None
    
    if status.strip().lower() not in ["disponivel", "emprestado"]:
        print("Status inválido!")
        return None
    
    autores = listar("autores")
    
    autor = None
    
    for autor_item in autores:
        if autor_item["nome"] == nome_autor:
            autor = autor_item
            break

    return {
        "id": len(listar("livros")) + 1,
        "titulo": titulo.strip(),
        "autor": autor,
        "status": status.strip().lower()
    }

def processar_criacao_do_livro(dados: dict) -> bool:

    """
    Função destinada a chamar as funções de validação e retorno do 'autor' e 'livro',
    efetuando, com esses dicionários, a operação de salvar no shelve.

    - Retorna False quando:
        - Informação do autor é inválida
        - Informação do livro é inválida
    
    - Retorna True quando:
        - Salva o livro
    """
    
    autor = montar_autor(dados["autor"])
    if not autor:
        return False
    
    if not buscar("autores", "nome", autor["nome"]):
        salvar("autores", autor)
    
    livro = montar_livro(dados["titulo"], dados["autor"], "disponivel")
    if not livro:
        return False
    
    salvar("livros", livro)
    print("Livro cadastrado com sucesso!")
    return True


def processar_busca_livros_pelo_status(status: str) -> bool:

    """
    Função destinada a buscar todos os livros com determinado status:
    'disponivel' ou 'emprestado'\n

    - Retorna False quando:
        - Não há livros com o status passado por argumento
        - Informação do livro é inválida
    
    - Retorna True quando:
        - Há pelo menos um livro salvo
    """
    
    livros = buscar_todos("livros", "status", status)

    saida = ""

    if not livros:
        print("Nenhum livro encontrado!")
        return False
    
    for livro in livros:
        dado = ""
        dado += f"\nLivro de ID: {livro["id"]}\n"
        dado += f"Titulo: {livro["titulo"]}\n"
        dado += f"Autor: {livro["autor"]["nome"]}\n"

        saida += formatar_tabela(dado)

    print(saida)
    return True

def processar_busca_de_livro_pelo_titulo(dados: dict):

    """
    Função destinada a buscar um livro pelo título\n

    - Se encontrar:
        - Imprime as informações do livro
    - Se não encontrar:
        - Imprime 'Não há livro com esse título'
    
    - Retorna True quando:
        - Há pelo menos um livro salvo
    """
    
    titulo = dados["titulo"]

    livro = buscar("livros", "titulo", titulo)

    saida = ""
    
    if livro: 
        saida += f"\nLivro de ID: {livro["id"]}\n"
        saida += f"Titulo: {livro["titulo"]}\n"
        saida += f"Autor: {livro["autor"]["nome"]}\n"

        print(formatar_tabela(saida))
        return
    print("Não há livro com esse titulo!")

    
def processar_exclusao_de_livro(dados: dict):

    """
    Função destinada a buscar um livro pelo excluir um livro\n

    - Pode receber:
        - Um dicionário com uma chave "id"
        - Um dicionário com uma chave "titulo"

    - Se excluir:
        - Imprime 'Livro excluido com sucesso!'
    - Se não excluir:
        - Imprime 'Erro na exclusão do livro!'
    """
    
    campo = "titulo"
    valor = dados.get("titulo")

    id = dados.get("id")
    
    if id:
        campo = "id"
        valor = int(id)

    if excluir("livros", campo, valor):
        print("Livro excluido com sucesso!")
        return True

    print("Erro na exclusão do livro!")
    return False
    

