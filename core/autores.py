from ui.tabela import formatar_tabela
from data.db import buscar, listar


def criar_autor(nome: str) -> dict | None:
    if len(nome.replace(" ", "")) < 1:
        print("Nome do autor muito curto!")
        return None
    
    nome = nome.strip()
    
    autor_existente = buscar("autores", "nome", nome)
    
    if autor_existente:
        return autor_existente
    
    autores = listar("autores")
    
    return {
        "nome": nome,
        "id": len(autores) + 1
    }

def processar_busca_de_livros_de_um_autor_pelo_nome_do_autor(dados: dict) -> bool:

    """
    Função destinada a buscar e imprimir os livros de um autor buscado pelo seu nome
    """
    
    autor = buscar("autores", "nome", dados["nome"])
    
    if not autor:
        print("Autor não encontrado!")
        return False
    
    livros = [livro for livro in listar("livros") if livro["autor"]["id"] == autor["id"]]
    
    if not livros:
        print(f"Nenhum livro de {autor["nome"]} encontrado!")
        return False
    
    saida = f"\nLivros de {autor["nome"]}:\n"
    for livro in livros:
        dado = f"ID: {livro["id"]} - {livro["titulo"]}\n"
        saida += formatar_tabela(dado)
        
    print(saida)
    return True