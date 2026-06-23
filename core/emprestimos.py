from data.db import atualizar, buscar, listar


def processar_emprestimo(dados: dict) -> bool:
    """
    Função destinada a atualizar o status de um determinado livro para 'emprestado'

    Se o livro existir e o status for 'disponivel':
        - Atualiza o status
        - Imprime 'Empréstimo de livro registrado com sucesso!'
        - retorna True

    Se o livro não existir:
        - Imprime 'Livro não encontrado!'
        - Retorna False

    Se o status do livro for 'emprestado':
        - Imprime 'Livro não está disponível!'
        - Retorna False
    """

    livro = buscar("livros", "id", int(dados["id"]))

    if not livro:
        print("Livro não encontrado!")
        return False

    if livro["status"] != "disponivel":
        print(
            "Erro: O livro não pode ser emprestado! O livro não está disponível, está emprestado."
        )
        return False

    atualizar("livros", "id", livro["id"], {"status": "emprestado"})
    print(f"Empréstimo de '{livro['titulo']}' registrado com sucesso!")
    return True


def processar_devolucao(dados: dict) -> bool:
    """
    Função destinada a atualizar o status de um determinado livro para 'disponivel'

    Se o livro existir e o status for 'emprestado':
        - Atualiza o status
        - Imprime 'Devolução de livro registrada com sucesso!'
        - retorna True

    Se o livro não existir:
        - Imprime 'Livro não encontrado!'
        - Retorna False

    Se o status do livro for 'disponivel':
        - Imprime 'Livro não está emprestado!'
        - Retorna False
    """

    livro = buscar("livros", "id", int(dados["id"]))

    if not livro:
        print("Livro não encontrado!")
        return False

    if livro["status"] != "emprestado":
        print(
            "Erro: O livro não pode ser devolvido! O livro não está emprestado, está disponível."
        )
        return False

    atualizar("livros", "id", livro["id"], {"status": "disponivel"})
    print(f"Devolução de '{livro['titulo']}' registrada com sucesso!")
    return True

