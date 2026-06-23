from core.id import gerar_novo_id
from data.db import buscar, listar
from ui.formatador_saidas import exibir_livros_de_cada_autor, exibir_mensagem, formatar_tabela


def criar_autor(nome: str) -> dict:
    """
    Função destinada a criar o dicionário que representa um autor
    """
    
    nome = nome.strip()

    autor_existente = buscar("autores", "nome", nome)

    if autor_existente:
        return autor_existente

    autores = listar("autores")

    return {"nome": nome, "id": gerar_novo_id(autores)}


def processar_busca_de_livros_de_um_autor_pelo_nome_do_autor(dados: dict) -> bool:
    """
    Função destinada a buscar e imprimir os livros de um autor buscado pelo seu nome
    """

    autor = buscar("autores", "nome", dados["nome"])

    if not autor:
        exibir_mensagem("Autor não encontrado!\n")
        return False

    livros = [
        livro for livro in listar("livros") if livro["autor"]["id"] == autor["id"]
    ]

    if not livros:
        exibir_mensagem(f"Nenhum livro de {autor['nome']} encontrado!")
        return False

    exibir_livros_de_cada_autor(livros, [autor])
    return True

def obter_autores_sem_livros(lista_livros: list[dict], lista_autores: list[dict]) -> list[dict]:
    """
    Função destinada a retornar apenas os autores que não possuem nenhuma associação com livros.
    """
    
    ids_autores_com_livros = {livro["autor"]["id"] for livro in lista_livros}
    
    autores_sem_livros = [
        autor for autor in lista_autores 
        if autor["id"] not in ids_autores_com_livros
    ]
    
    return autores_sem_livros

def processar_exclusao_do_autor_que_nao_possui_livros():
    """
    Função destinada a fazer a exclusão de autores que não possuem livros
    """
    
    autores = listar("autores")
    livros = listar("livros")
    
    autores_para_excluir = obter_autores_sem_livros(livros, autores)
    
    if not autores_para_excluir:
        exibir_mensagem("Todos os autores possuem livros associados.", erro=True)
        return

    exibir_mensagem("Autores encontrados sem livros associados:")
    for autor in autores_para_excluir:
        print(formatar_tabela(f"{autor['nome']} (ID: {autor['id']})"))