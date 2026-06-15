from core.livros import processar_busca_livros_pelo_status
from data.db import buscar_todos, listar
from ui.componentes import formulario_cadastro_autor, menu_selecionar_autor, menu_selecionar_livro


def exibir_livros_por_status(status: str) -> str | None:
    livros = buscar_todos("livros", "status", status)
    
    if not livros:
        print("Nenhum livro encontrado!")
        return None
    
    menu_selecionar_livro.limpar_opcoes()
    for livro in livros:
        menu_selecionar_livro.add_opcao(
            f"{livro["titulo"]} - {livro["autor"]["nome"]}",
            acao=lambda livro=livro: livro 
        )
    
    return menu_selecionar_livro.exibir()


def exibir_menu_selecionar_autor():
    menu_selecionar_autor.limpar_opcoes()
    
    autores = listar("autores")
    for autor in autores:
        menu_selecionar_autor.add_opcao(autor["nome"])
    
    return menu_selecionar_autor.exibir()
    
def exibir_autor() -> str:
    autores = listar("autores")
    
    menu_selecionar_autor.limpar_opcoes()
    menu_selecionar_autor.add_opcao("Cadastrar novo autor")
    
    for autor in autores:
        menu_selecionar_autor.add_opcao(autor["nome"])
    
    escolha = menu_selecionar_autor.exibir()
    
    if escolha is None:
        return "0"
    
    if escolha == "Cadastrar novo autor":
        dados = formulario_cadastro_autor.exibir()
        if dados is None:
            return "0"
        return dados["nome"]
    
    return escolha

def exibir_livros_disponiveis() -> str:
    processar_busca_livros_pelo_status("disponivel")
    return input("ID do livro: ").strip()

def exibir_livros_emprestados() -> str:
    processar_busca_livros_pelo_status("emprestado")
    return input("ID do livro: ").strip()