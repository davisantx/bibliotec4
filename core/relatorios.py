from data.db import buscar_todos, listar
from ui.formatador_saidas import (
    exibir_livros,
    exibir_livros_de_cada_autor,
    exibir_mensagem,
    exibir_quantidade_de_livros_disponiveis_e_emprestados,
    exibir_todos_os_dados_registrados_na_biblioteca,
)


def mostrar_os_livros_recentes() -> None:
    """
    Função destinada a buscar todos os livros salvos e exibir pela
    ordem dos mais recentes.\n

    - Se não houverem livros salvos ainda:
        - Imprime 'Não existem livros cadastrados ainda!'
    - Se houver pelo menos um livro cadastrado:
        - Imprime as informações de cada livro pela ordem dos mais recentes
    """

    livros = listar("livros")

    if not livros:
        exibir_mensagem("Não existem livros cadastrados ainda!", erro=True)
        return

    livros_pela_ordem_dos_mais_recentes = livros[::-1]

    exibir_livros(livros_pela_ordem_dos_mais_recentes)


def mostrar_quais_livros_cada_autor_tem_na_biblioteca() -> None:
    """
    Função destinada a buscar todos os livros de cada autor registrado,
    exibindo o nome dos autores, seus livros e a quantidade de livros de cada um\n

    - Se não houverem livros salvos ainda:
        - Imprime 'Não existem livros cadastrados ainda!'
    - Se houver pelo menos um livro cadastrado:
        - Imprime as informações de cada livro pela ordem dos mais recentes
    """

    autores = listar("autores")
    livros = listar("livros")

    if not autores:
        exibir_mensagem("Não existem autores cadastrados ainda!", erro=True)
        return

    exibir_livros_de_cada_autor(livros, autores)


def mostrar_numero_de_livros_disponiveis_e_emprestados() -> None:
    """
    Função destinada a imprimir quanto livros estão disponíveis e emprestados.

    1. Busca todos os livros com status disponivel
    2. Busca todos os livros com status emprestado
    3. Imprime a quantidade de livros com status disponivel
    4. Imprime a quantidade de livros com status emprestado
    """

    disponiveis = buscar_todos("livros", "status", "disponivel")
    emprestados = buscar_todos("livros", "status", "emprestado")

    exibir_quantidade_de_livros_disponiveis_e_emprestados(disponiveis, emprestados)


def mostrar_todos_os_dados_registrados_da_biblioteca() -> None:
    """
    Função destinada a mostrar todos os dados registrados da biblioteca de modo formatado ao usuário.
    """

    livros = listar("livros")

    if not livros:
        exibir_mensagem("Não há livros!", erro=True)
        return

    exibir_todos_os_dados_registrados_na_biblioteca(livros)
    return
