def formatar_tabela(dados: str) -> str:
    """
    Formata os dados para saída do sistema.

    Exemplo:
    ```
    -----------------------------------
    Título: Memorias Postumas de Bras Cubas
    Autor: Machado de Assis
    ID: 1
    -----------------------------------
    ```
    """

    saida = "\n"

    saida += "-" * 60
  
    saida += f"\n{dados}\n"
 
    saida += "-" * 60

    saida += "\n"

    return saida


def exibir_input_campo(titulo_input: str):
    print("-" * 40)
    saida = input(f"{titulo_input}: ")
    print("-" * 40)
    return saida

def exibir_mensagem(mensagem: str, erro: bool=False):
    saida = f"{formatar_tabela(f"\033[32m[Sucesso!]: {mensagem}\033[m")}"
    
    if erro:
        saida = f"{formatar_tabela(f"\033[31m[Ops!]: {mensagem}\033[m")}"

    print(saida)



def exibir_livros(livros: list[dict]):
    """
    Função destinada a printar os livros
    """
    saida = ""
    for livro in livros:
        dado = ""
        dado += f"Livro de ID: {livro['id']}\n"
        dado += f"Titulo: {livro['titulo']}\n"
        dado += f"Autor: {livro['autor']['nome']}\n"
        saida += formatar_tabela(dado)

    print(saida)


def exibir_livros_de_cada_autor(livros: list[dict], autores: list[dict]):
    """
    Função destinada a printar os livros de cada autor
    """
    saida = ""

    for autor in autores:
        dado = ""
        livros_do_autor = [
            livro for livro in livros if livro["autor"]["id"] == autor["id"]
        ]
        dado += f"{autor['nome']} → {len(livros_do_autor)} livro(s)\n"

        for livro in livros_do_autor:
            dado += f"  - {livro['titulo']}\n"

        saida += formatar_tabela(dado)

    print(saida)


def exibir_quantidade_de_livros_disponiveis_e_emprestados(
    disponiveis: list[dict], emprestados: list[dict]
):
    """
    Função destinada a printar a quantidade de livros disponíveis e emprestados
    """
    saida = f"Disponíveis: {len(disponiveis)}\n"
    saida += f"Emprestados: {len(emprestados)}\n"

    print(formatar_tabela(saida))


def exibir_todos_os_dados_registrados_na_biblioteca(livros: list[dict]):
    """
    Função destinada a printar todos os dados registrados na biblioteca de modo organizado
    """
    saida = ""
    for livro in livros:
        dado = ""
        autor = livro["autor"]

        dado += f"Título: {livro['titulo']}"
        dado += "\nAutor: "
        dado += f"\n    Nome: {autor['nome']}"
        dado += f"\n    ID: {autor['id']}"
        dado += f"\nStatus: {livro['status']}"
        dado += f"\nID: {livro['id']}\n"

        saida += formatar_tabela(dado)

    print(saida)
