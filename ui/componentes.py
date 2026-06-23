from ui.menu import Menu, Formulario

# Menu principal
menu_inicial = Menu("Bibliotec4 - Seu Sistema de Gerenciamento de Biblioteca")

# Cadastro
menu_cadastro = Menu("Cadastro")

# Busca
menu_de_busca = Menu("Busca de livros")

menu_de_busca_pelo_status = Menu("Busca de livros pelo status")
formulario_busca_titulo = Formulario("Insira o título")

# Exclusão
menu_excluir = Menu("Exclusão de livro")

# Relatórios
menu_relatorios = Menu("Relatórios")

#
menu_emprestimos_e_devolucoes = Menu("Emprestimos e devoluções")


menu_selecionar_autor = Menu("Selecione o autor")

menu_selecionar_livro = Menu("Selecione o livro")

formulario_cadastro_autor = Formulario("Insira as informações do autor")


menu_selecionar_livro = Menu("Selecione o livro")

menu_selecione_o_autor_sem_livros_para_excluir = Menu("Selecione um dos autores sem livros para excluir")
menu_exclusao_de_autor = Menu("Excluir autor")


formulario_emprestimo = Formulario("Registrar empréstimo")
formulario_devolucao = Formulario("Registrar devolução")

formulario_excluir_titulo = Formulario("Excluir por título")
formulario_excluir_id = Formulario("Excluir por ID")


formulario_cadastro_livro = Formulario("Insira as informações do livro")
formulario_cadastro_autor = Formulario("Insira as informações do autor")

menu_selecionar_autor = Menu("Selecione o autor")
formulario_busca_nome_autor = Formulario("Busca dos livros do autor pelo nome")