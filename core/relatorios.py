from ui.tabela import formatar_tabela
from data.db import buscar_todos, listar


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
        print("Não existem livros cadastrados ainda!")
        return
    
    autores = listar("autores")
    saida = ""
    
    for livro in livros[::-1]:
        dado = ""

        autor = None
        
        for a in autores:
            if a["id"] == livro["autor"]["id"]:
                autor = a
                break
 
        dado += f"Título: {livro["titulo"]}\n"
        dado += f"Autor: {autor["nome"] if autor else "Desconhecido"}\n"
        dado += f"ID: {livro["id"]}\n"

        saida += formatar_tabela(dado)

    print(saida)

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
        print("Não existem autores cadastrados ainda!")
        return
    
    saida = ""
    
    for autor in autores:
        dado = ""
        livros_do_autor = [livro for livro in livros if livro["autor"]["id"] == autor["id"]]
        dado += f"{autor["nome"]} → {len(livros_do_autor)} livro(s)\n"
        
        for livro in livros_do_autor:
            dado += f"  - {livro["titulo"]}\n"
        
        saida += formatar_tabela(dado)
            
    print(saida)




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

    saida = f"Disponíveis: {len(disponiveis)}\n"
    saida += f"Emprestados: {len(emprestados)}"

    print(formatar_tabela(saida))

def mostrar_todos_os_dados_registrados_da_biblioteca() -> None:

    """
    Função destinada a mostrar todos os dados registrados da biblioteca de modo formatado ao usuário.
    """
    
    livros = listar("livros")
    
    if not livros:
        print("Não há livros!")
        return

    saida = ""
    for livro in livros:
        dado = ""
        autor = livro["autor"]

        dado += f"Título: {livro["titulo"]}"
        dado += "\nAutor: "
        dado += f"\n    Nome: {autor["nome"]}"
        dado += f"\n    ID: {autor["id"]}"
        dado += f"\nStatus: {livro["status"]}"
        dado += f"\nID: {livro["id"]}\n"

        saida += formatar_tabela(dado)
        
    print(saida)
    return