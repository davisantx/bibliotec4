from core.autores import processar_busca_de_livros_de_um_autor_pelo_nome_do_autor
from core.emprestimos import processar_devolucao, processar_emprestimo
from core.livros import processar_busca_de_livro_pelo_titulo, processar_busca_livros_pelo_status, processar_criacao_do_livro, processar_exclusao_de_livro
from core.relatorios import mostrar_numero_de_livros_disponiveis_e_emprestados, mostrar_os_livros_recentes, mostrar_quais_livros_cada_autor_tem_na_biblioteca, mostrar_todos_os_dados_registrados_da_biblioteca
from ui.coletores import exibir_autor, exibir_livros_disponiveis, exibir_livros_emprestados
from ui.componentes import formulario_busca_nome_autor, formulario_busca_titulo, formulario_cadastro_autor, formulario_cadastro_livro, formulario_devolucao, formulario_emprestimo, formulario_excluir_id, formulario_excluir_titulo, menu_cadastro, menu_de_busca, menu_de_busca_pelo_status, menu_emprestimos_e_devolucoes, menu_excluir, menu_inicial, menu_relatorios, menu_selecionar_autor, menu_selecionar_livro


def configurar_menus():

    """
    Função destinada a popular os Menus e Formulários com a adição de opções ou campos,
    bem como suas respectivas acões.
    """

    
    # Menu para registrar emprestimos e/ou devoluções
    (menu_emprestimos_e_devolucoes
        .add_opcao("Registrar um empréstimo", acao=formulario_emprestimo.exibir)
        .add_opcao("Registrar uma devolução", acao=formulario_devolucao.exibir)
        .add_navegacao("Voltar"))
    
    
    # Menu principal (inicial), exibe todas as funcionalidades principais do sistema
    (menu_inicial
        .add_opcao("Cadastrar", acao=menu_cadastro.exibir)
        .add_opcao("Buscar", acao=menu_de_busca.exibir)
        .add_opcao("Emprestimos e devoluções", acao=menu_emprestimos_e_devolucoes.exibir)
        .add_opcao("Excluir", acao=menu_excluir.exibir)
        .add_opcao("Relatórios", acao=menu_relatorios.exibir))

    # Menu para cadastrar livro
    (menu_cadastro
        .add_opcao("Cadastrar livro", acao=formulario_cadastro_livro.exibir)
        .add_navegacao("Voltar"))
    
    
    # Menu de busca pelo titulo/status
    (menu_de_busca
        .add_opcao("Buscar livro pelo título", acao=formulario_busca_titulo.exibir)
        .add_opcao("Buscar livro pelo status", acao=menu_de_busca_pelo_status.exibir)
        .add_opcao("Buscar livros de um autor pelo nome do autor", acao=formulario_busca_nome_autor.exibir)
        .add_navegacao("Voltar"))
    
    # Menu de busca pelo status
    (menu_de_busca_pelo_status
        .add_opcao("Disponível", acao=lambda: processar_busca_livros_pelo_status("disponivel"))
        .add_opcao("Emprestado", acao=lambda: processar_busca_livros_pelo_status("emprestado"))
        .add_navegacao("Voltar"))
    
    # Menu de exclusão do livro
    (menu_excluir
        .add_opcao("Excluir por ID", acao=formulario_excluir_id.exibir)
        .add_opcao("Excluir pelo título", acao=formulario_excluir_titulo.exibir)
        .add_navegacao("Voltar"))
    
    
    # Menu de relatórios
    (menu_relatorios
        .add_opcao("Número de livros disponíveis e emprestados", mostrar_numero_de_livros_disponiveis_e_emprestados)
        .add_opcao("Ver os últimos livros adicionados", mostrar_os_livros_recentes)
        .add_opcao("Ver quantos livros cada autor tem na biblioteca", mostrar_quais_livros_cada_autor_tem_na_biblioteca)
        .add_opcao("Ver todos os dados registrados da biblioteca", mostrar_todos_os_dados_registrados_da_biblioteca)
        .add_navegacao("Voltar"))
    
    # Formulário para inserir o ID do livro disponível que será efetuado o emprestimo
    (formulario_emprestimo
        .add_campo("id", "ID do livro", input_personalizado=exibir_livros_disponiveis)
        .ao_confirmar(processar_emprestimo))
    
    # Formulário para inserir o ID do livro emprestado que será efetuado a devolução
    (formulario_devolucao
        .add_campo("id", "ID do livro", input_personalizado=exibir_livros_emprestados)
        .ao_confirmar(processar_devolucao))
    
    formulario_cadastro_autor.add_campo("nome", "Nome do autor")
    
    # Formulário pra inserir as informações do livro no cadastro
    (formulario_cadastro_livro
        .add_campo("titulo", "Título do livro")
        .add_campo("autor", "Autor", input_personalizado=exibir_autor)
        .ao_confirmar(processar_criacao_do_livro))
        
    # Formulário pra inserir o título pra efetuar a busca do livro pelo título
    (formulario_busca_titulo
        .add_campo("titulo", "Título")
        .ao_confirmar(processar_busca_de_livro_pelo_titulo))
    
    # Formulário pra inserir o título pra efetuar a exclusão do livro pelo título
    (formulario_excluir_titulo
        .add_campo("titulo", "Insira o título")
        .ao_confirmar(processar_exclusao_de_livro))
    
    # Formulário pra inserir o ID pra efetuar a exclusão do livro pelo ID
    (formulario_excluir_id
        .add_campo("id", "Insira o ID")
        .ao_confirmar(processar_exclusao_de_livro))
    
    
    # Formulário para inserir o nome do autor para efetuar uma busca
    (formulario_busca_nome_autor
        .add_campo("nome", "Insira o nome do autor")
        .ao_confirmar(processar_busca_de_livros_de_um_autor_pelo_nome_do_autor)
    )


    # Adiciona navegação no menu de selecionar livro
    menu_selecionar_livro.add_navegacao("Voltar")

    # Adiciona navegação no menu de selecionar autor
    menu_selecionar_autor.add_navegacao("Voltar")