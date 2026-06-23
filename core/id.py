def gerar_novo_id(lista_de_dados: list[dict]) -> int:
    """
    Função destinada a gerar um ID único e sequencial baseado 
    no maior ID existente na lista.
    """
    if not lista_de_dados:
        return 1
        
    return max(item["id"] for item in lista_de_dados) + 1