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
    
    saida += "-" * 35
    
    saida += f"\n{dados}"

    saida += "-" * 35
    
    saida += "\n"

    return saida
    