from data.db import atualizar, buscar


def processar_emprestimo(dados: dict) -> bool:
    livro = buscar("livros", "id", int(dados["id"]))
    
    if not livro:
        print("Livro não encontrado!")
        return False
    
    if livro["status"] != "disponivel":
        print("Livro não está disponível!")
        return False
    
    atualizar("livros", "id", livro["id"], {"status": "emprestado"})
    print(f"Empréstimo de '{livro["titulo"]}' registrado com sucesso!")
    return True

def processar_devolucao(dados: dict) -> bool:
    livro = buscar("livros", "id", int(dados["id"]))
    
    if not livro:
        print("Livro não encontrado!")
        return False
    
    if livro["status"] != "emprestado":
        print("Livro não está emprestado!")
        return False
    
    atualizar("livros", "id", livro["id"], {"status": "disponivel"})
    print(f"Devolução de '{livro["titulo"]}' registrada com sucesso!")
    return True