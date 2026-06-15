from core.livros import processar_busca_livros_pelo_status
from data.db import listar
from ui.componentes import formulario_cadastro_autor, menu_selecionar_autor


def exibir_autor() -> str:

    """
    Função que representa um input personalizado para o formulário
    de cadastro de livro
    
    Ela exibe um menu, onde cada autor existente na biblioteca é uma opção
    selecionável;

    Fica algo como:

    ```
    SELECIONE O AUTOR
    1. Cadastrar novo autor
    2. Machado de Assis
    3. Carlos Drummond de Andrade
    0. Voltar
    
    Escolha: 1
    ```
    """
    
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

    """
    Função que representa um input personalizado para o formulário
    de emprestimo
    
    Ela exibe todos os livros disponiveis para emprestimo.

    Logo após pede o ID do livro para registrar o empréstimo

    ```
    REGISTRAR EMPRÉSTIMO
    (Digite 0 para voltar)
    
    -----------------------------------
    Livro de ID: 1
    Titulo: Memorias Postumas de Bras Cubas
    Autor: Machado de Assis
    -----------------------------------
    -----------------------------------
    Livro de ID: 4
    Titulo: Alguma Poesia
    Autor: Carlos Drummond de Andrade
    -----------------------------------
    
    ID do livro: 4
    Empréstimo de 'Alguma Poesia' registrado com sucesso!
    ```
    """
    
    processar_busca_livros_pelo_status("disponivel")
    return input("ID do livro: ").strip()

def exibir_livros_emprestados() -> str:

    """
    Função que representa um input personalizado para o formulário
    de emprestimo
    
    Ela exibe todos os livros disponiveis para emprestimo.

    Logo após pede o ID do livro para registrar o empréstimo

    ```
    REGISTRAR DEVOLUÇÃO
    (Digite 0 para voltar)
    
    -----------------------------------
    Livro de ID: 4
    Titulo: Alguma Poesia
    Autor: Carlos Drummond de Andrade
    -----------------------------------
    
    ID do livro: 4
    Devolução de 'Alguma Poesia' registrada com sucesso!
    ```
    """
    
    processar_busca_livros_pelo_status("emprestado")
    return input("ID do livro: ").strip()