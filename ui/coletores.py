from core.livros import processar_busca_livros_pelo_status
from data.db import listar
from ui.componentes import formulario_cadastro_autor, menu_selecionar_autor
from ui.instrucoes import Instrucao


def exibir_autor() -> str:

    """
    Função que representa um input personalizado para o formulário
    de cadastro de livro

    Ela utiliza um menu para receber a entrada.
    
    Nesse menu, cada autor existente na biblioteca é uma opção
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

    opcao_voltar = "0"
    
    autores = listar("autores")
    
    menu_selecionar_autor.limpar_opcoes()
    menu_selecionar_autor.add_opcao("Cadastrar novo autor")
    
    for autor in autores:
        menu_selecionar_autor.add_opcao(autor["nome"])
    
    instrucao_menu_selecionar_autor = menu_selecionar_autor.exibir()
    
    if instrucao_menu_selecionar_autor == Instrucao.VOLTAR:
        return opcao_voltar
       
    if instrucao_menu_selecionar_autor == Instrucao.CONFIRMAR:
        texto_da_opcao_selecionada = menu_selecionar_autor.get_opcao_selecionada()

        if texto_da_opcao_selecionada == "Cadastrar novo autor":
            instrucao_formulario = formulario_cadastro_autor.exibir()

            if instrucao_formulario == Instrucao.VOLTAR:
                return opcao_voltar
            
            dados = formulario_cadastro_autor.get_dados()
            return dados["nome"]
            
        if texto_da_opcao_selecionada is not None:         
            return texto_da_opcao_selecionada
        
    return opcao_voltar
    
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
    return input("ID do livro: ")

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
    return input("ID do livro: ")