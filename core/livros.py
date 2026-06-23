from core.autores import criar_autor
from core.id import gerar_novo_id
from data.db import buscar, buscar_todos, excluir, listar, salvar
from ui.formatador_saidas import exibir_livros, exibir_mensagem


def criar_livro(titulo: str, nome_autor: str, status: str) -> dict:
    """
    Função destinada a:
        - Receber os dados do livro
        - Aplicar validação
        - E retornar o dicionário que representa o livro caso passe na validação

    Caso o título seja curto demais:
        - Imprime 'Título muito curto!'
        - Retorna None

    Caso o status não seja 'disponivel' ou 'emprestado':
        - Imprime 'Status inválido!'
        - Retorna None
    """

    autores = listar("autores")

    autor = None

    # Busca se o autor já existe
    for autor_item in autores:
        if autor_item["nome"] == nome_autor:
            autor = autor_item
            break

    # Retorna dicionário que representa o Autor
    return {
        "id": gerar_novo_id(listar("livros")),
        "titulo": titulo.strip(),
        "autor": autor,
        "status": status.strip().lower(),
    }


def processar_criacao_do_livro(dados: dict) -> bool:
    """
    Função destinada a efetuar a operação de salvar no shelve.
    """

    if len(dados["titulo"]) < 4:
        exibir_mensagem("Título muito curto!", erro=True)
        return False

    if len(dados["titulo"]) > 79:
        exibir_mensagem("Título muito longo!", erro=True)
        return False
        
    autores = listar("autores")
    nomes_existentes = {autor["nome"].lower() for autor in autores}
    nome_recebido = dados["autor"]
    
    
    if nome_recebido.lower() not in nomes_existentes:
        autor = criar_autor(nome_recebido)
        
        if len(autor["nome"]) < 3:
            exibir_mensagem("Nome do autor curto demais!", erro=True)
            return False
            
        salvar("autores", autor)


    titulo = dados["titulo"]
    livro = criar_livro(titulo, dados["autor"], "disponivel")
    salvar("livros", livro)
    
    exibir_mensagem(f"Livro '{titulo}' cadastrado com sucesso!")
    return True


def processar_busca_livros_pelo_status(status: str) -> bool:
    """
    Função destinada a buscar todos os livros com determinado status:
    'disponivel' ou 'emprestado'\n

    - Retorna False quando:
        - Não há livros com o status passado por argumento
        - Informação do livro é inválida

    - Retorna True quando:
        - Há pelo menos um livro salvo
    """

    livros = buscar_todos("livros", "status", status)

    if not livros:
        exibir_mensagem("Nenhum livro encontrado!", erro=True)
        return False

    exibir_livros(livros)
    return True


def processar_busca_de_livro_pelo_titulo(dados: dict) -> bool:
    """
    Função destinada a buscar um livro pelo título\n

    - Se encontrar:
        - Imprime as informações do livro
    - Se não encontrar:
        - Imprime 'Não há livro com esse título!'
    """

    titulo = dados["titulo"]
    
    livro = buscar("livros", "titulo", titulo)

    if livro:
        exibir_livros([livro])
        return True

    exibir_mensagem("Não há livro com esse titulo!", erro=True)
    return False


def processar_exclusao_de_livro(dados: dict) -> bool:
    """
    Função destinada excluir um livro\n

    - Pode receber:
        - Um dicionário com uma chave "id"
        - Um dicionário com uma chave "titulo"
    - Se conseguir excluir:
        - Imprime 'Livro excluido com sucesso!'
        - Retorna True
    - Se não conseguir excluir:
        - Imprime 'Erro na exclusão do livro!'
        - Retorna False
    """

    campo = "titulo"
    valor = dados.get(campo)

    id = dados.get("id")

    if id:
        campo = "id"
        valor = int(id)

    livro = buscar("livros", campo, valor)
    
    if livro is None:
        exibir_mensagem("Erro na exclusão do livro!")
        return False

    
    if excluir("livros", campo, valor):
        exibir_mensagem(f"Livro '{livro["titulo"]}' excluído com sucesso!")
        return True

    exibir_mensagem(f"Erro na exclusão do livro '{livro["titulo"]}'!", erro=True)
    return False
