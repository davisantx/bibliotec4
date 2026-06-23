from core.autores import obter_autores_sem_livros, processar_busca_de_livros_de_um_autor_pelo_nome_do_autor
from core.livros import processar_busca_livros_pelo_status
from data.db import excluir, listar
from ui.componentes import formulario_cadastro_autor, menu_selecionar_autor, menu_selecione_o_autor_sem_livros_para_excluir
from ui.estados import Estado
from ui.formatador_saidas import exibir_input_campo, exibir_livros_de_cada_autor, exibir_mensagem, formatar_tabela

"""
Inputs personalizados

Alguns apenas inputs

Alguns misturam Menus e Formulário junto de lógica de validação
"""

def exibir_lista_com_autores_existentes() -> str:
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

    estado_menu_selecionar_autor = menu_selecionar_autor.exibir()

    if estado_menu_selecionar_autor == Estado.CANCELADO:
        return opcao_voltar

    if estado_menu_selecionar_autor == Estado.SUCESSO:
        texto_da_opcao_selecionada = menu_selecionar_autor.get_opcao_selecionada()

        if texto_da_opcao_selecionada == "Cadastrar novo autor":
            estado_formulario = formulario_cadastro_autor.exibir()

            if estado_formulario == Estado.CANCELADO:
                return opcao_voltar

            dados = formulario_cadastro_autor.get_dados()
            nome_formatado = " ".join(dados["nome"].split())

            nomes_existentes = {" ".join(autor["nome"].split()).lower() for autor in autores}

            # só serve pra nomes inseridos no campo input
            if nome_formatado.lower() in nomes_existentes:
                exibir_mensagem(f"Erro: O autor '{nome_formatado}' já está cadastrado!", erro=True)
                return opcao_voltar

            return nome_formatado

        if texto_da_opcao_selecionada is not None:
            return texto_da_opcao_selecionada

    return opcao_voltar

def exibir_lista_com_autores_que_podem_ser_excluidos() -> str:
    """
    Função destinada a listar os autores que não possuem nenhum livro e exibe o menu e faz a ação.
    """
    
    opcao_voltar = "0"

    autores_sem_livros = obter_autores_sem_livros(listar("livros"), listar("autores"))

    if not autores_sem_livros:
        exibir_mensagem("Todos os autores possuem livros associados. Não há o que excluir.", erro=True)
        return opcao_voltar

    menu_selecione_o_autor_sem_livros_para_excluir.limpar_opcoes()
    for autor_sem_livro in autores_sem_livros:
        menu_selecione_o_autor_sem_livros_para_excluir.add_opcao(autor_sem_livro["nome"])

    estado_menu = menu_selecione_o_autor_sem_livros_para_excluir.exibir()

    if estado_menu == Estado.CANCELADO:
        return opcao_voltar

    if estado_menu == Estado.SUCESSO:
        texto_da_opcao_selecionada = menu_selecione_o_autor_sem_livros_para_excluir.get_opcao_selecionada()

        if texto_da_opcao_selecionada is not None:

            sucesso_ao_apagar = excluir("autores", "nome", texto_da_opcao_selecionada)
                
            if sucesso_ao_apagar:
                exibir_mensagem(f"Autor '{texto_da_opcao_selecionada}' excluído com sucesso!")
            else:
                exibir_mensagem(f"Erro: Não foi possível encontrar o autor '{texto_da_opcao_selecionada}'!\n", erro=True)
     
            return texto_da_opcao_selecionada

    return opcao_voltar

def excluir_todos_autores_sem_livros() -> str:
    """
    Função destinada a excluir todos os autores sem livros de uma vez.
    """

    opcao_voltar = "0"
    
    autores = listar("autores")
    livros = listar("livros")
    
    autores_para_excluir = obter_autores_sem_livros(livros, autores)
    
    if not autores_para_excluir:
        exibir_mensagem("Todos os autores atuais possuem livros associados. Não há o que excluir.", erro=True)
        return opcao_voltar
        
    quantidade_excluida = 0
    
    for autor in autores_para_excluir:
        sucesso = excluir(chave="autores", campo="id", valor=autor["id"])
        
        if sucesso:
            print(formatar_tabela(f"Autor '{autor["nome"]}' excluído.\n"))
            quantidade_excluida += 1
            
    exibir_mensagem(f"Operação concluída! {quantidade_excluida} autor(es) excluído(s) com sucesso!")
    
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
    print("\nLivros que estão disponíveis no momento:".upper())
    processar_busca_livros_pelo_status("disponivel")

    return exibir_input_campo("ID do livro")


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
    print("\nLivros que estão emprestados no momento:".upper())
    processar_busca_livros_pelo_status("emprestado")

    return exibir_input_campo("ID do livro")


def exibir_livros_para_excluir_pelo_titulo():
    exibir_livros_de_cada_autor(listar("livros"), listar("autores"))

    return exibir_input_campo("Insira o título")

