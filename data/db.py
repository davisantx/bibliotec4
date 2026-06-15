import shelve
import os

CAMINHO_BD = os.path.join("data", "biblioteca_dados")

def inicializar_banco() -> None:

    """
    Função destinada a inicializar o shelve, criando um arquivo no caminho salvo em CAMINHO_BD
    """
    
    try:
        with shelve.open(CAMINHO_BD, writeback=True) as db:
            if "livros" not in db:
                db["livros"] = []
            if "autores" not in db:
                db["autores"] = []
    except OSError as e:
        print(f"Erro ao inicializar banco: {e}")
        raise

def listar(chave: str) -> list[dict]:

    """
    Função destinada a obter dados de uma chave no dicionário do shelve.\n
    Caso haja erro, tenta-se inicializar o banco do shelve novamente.
    """
    
    with shelve.open(CAMINHO_BD) as db:
        return db.get(chave, [])

def salvar(chave: str, dados: dict) -> dict:

    """
    Função destinada para salvar dados no último item da lista de uma chave qualquer.
    """
    
    with shelve.open(CAMINHO_BD, writeback=True) as db:
        if chave not in db:
            db[chave] = []
        db[chave].append(dados)
        return dados

def buscar(chave: str, campo: str, valor) -> dict | None:

    """
    Função destinada para buscar um item a partir de uma chave, como:
        - "livros"
        - "autores"
        
    campo, como:
        - "titulo"
        - "id"
        
    valor, como:
        - "Vidas Secas" (titulo do livro)
        - 3 (id)
    """
    
    lista = listar(chave)
    
    if isinstance(valor, str):
        valor = valor.strip().lower()
    
    for item in lista:
        item_valor = item.get(campo)
        if isinstance(item_valor, str):
            item_valor = item_valor.strip().lower()
        if item_valor == valor:
            return item
    return None


def buscar_todos(chave: str, campo: str, valor) -> list[dict]:
    """
    Função destinada a buscar todos os itens que correspondem a um campo e valor
    na lista de alguma das chaves do dicionário do shelve.\n
    Pode ser usada pra buscar todos os livros de um autor, por exemplo.
    """
    
    saida = []
    lista = listar(chave)

    for item in lista:
        if item.get(campo) == valor:
            saida.append(item)
    
    return saida

def atualizar(chave: str, campo: str, valor, novos_dados: dict) -> bool:

    """
    Função destinada a atualizar dados
    """
    
    with shelve.open(CAMINHO_BD, writeback=True) as db:
        lista = db.get(chave, [])
        for item in lista:
            if item.get(campo) == valor:
                item.update(novos_dados)
                return True
        return False


def excluir(chave: str, campo: str, valor) -> bool:

    """
    Função destinada a excluir dados
    """
    
    with shelve.open(CAMINHO_BD, writeback=True) as db:
        lista = db.get(chave, [])
        nova_lista = [item for item in lista if item.get(campo) != valor]
        if len(nova_lista) == len(lista):
            return False
        db[chave] = nova_lista
        return True