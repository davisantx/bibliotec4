from abc import ABC, abstractmethod
from enum import Enum

class Sinal(Enum):
    CONTINUAR = "continuar"

class IO(ABC):
    
    """
    Classe abstrata herdada pelos componentes Menu e Formulário.
    """
    
    def __init__(self):
        self._titulo = "MENU"

    @abstractmethod
    def exibir(self) -> "None | IO | str | dict": pass


class Menu(IO):
    def __init__(self, titulo: str):
        self._titulo = titulo
        self._opcoes = []
        self._saida = None
        self.add_navegacao("Sair", exit)
        
    def add_opcao(self, texto: str, acao=None) -> "Menu":
        opcoes_normais = [opcao for opcao in self._opcoes if opcao[0] != 0]
        self._opcoes.append((len(opcoes_normais) + 1, texto, acao))
        return self

    def add_navegacao(self, texto: str, acao=None):
        self._opcoes.insert(0, (0, texto, acao))
        return self

    def limpar_opcoes(self) -> "Menu":
        self._opcoes = [opcao for opcao in self._opcoes if opcao[0] == 0]
        return self
    
    def exibir(self) -> str | None:

        """
        Exibe o título e opções do Menu
        """
        
        while True:
            saida = f"\n{self._titulo.upper()}\n"
            
            for atalho, texto, _ in self._opcoes:
                if atalho != 0:
                    saida += f"{atalho}. {texto}\n"
            
            sair_atalho, sair_texto, _ = self._opcoes[0]
            saida += f"{sair_atalho}. {sair_texto}\n"
            
            print(saida)
            
            resultado = self._processar()
            if resultado is not Sinal.CONTINUAR:
                return resultado
        
    def _processar(self) -> "str | None | Sinal":

        """
        Recebe a entrada do usuário, repetindo-a caso ocorra uma exceção ValueError

        1. Percorre as opções
        2. Se chegar na opção de escolha, ele verifica se o valor do atalho é 0
        3. Se for 0, retorna None
        
        """
        
        try:
            escolha = int(input("Escolha: ").strip())
        except ValueError:
            return Sinal.CONTINUAR

        for atalho, texto, acao in self._opcoes:
            if escolha == atalho:
                if atalho == 0:
                    return None
                if acao:
                    acao()
                    return Sinal.CONTINUAR
                return texto
        
        print("Opção inválida.")
        return Sinal.CONTINUAR
        

class Formulario(IO):
    def __init__(self, titulo: str):
        self._titulo = titulo
        self._campos = []
        self._dados = {}
        self._ao_submeter = None
        self._ao_concluir = None
    
    def ao_concluir(self, acao) -> "Formulario":
        self._ao_concluir = acao
        return self

    def add_campo(self, chave: str, label: str, input_personalizado=None) -> "Formulario":
        self._campos.append((chave, label, input_personalizado or (lambda: input(f"{label}: ").strip())))
        return self

    def ao_confirmar(self, ao_submeter) -> "Formulario":
        self._ao_submeter = ao_submeter
        return self

    def _exibir_titulo(self) -> None:
        print(f"\n{self._titulo.upper()}")
        print("(Digite 0 para voltar)\n")
    
    def _capturar_campos(self) -> bool:
        self._dados = {}
        for chave, label, input_personalizado in self._campos:
            valor = input_personalizado() if input_personalizado else input(f"{label}: ").strip()
            if valor == "0":
                return False
            self._dados[chave] = valor
        return True
    
    def _submeter(self) -> bool:
        if self._ao_submeter:
            resultado = self._ao_submeter(self._dados)
            return resultado is not False
        return True
    
    def exibir(self) -> dict | None:
        while True:
            self._exibir_titulo()
            
            if not self._capturar_campos():
                return None
            
            if self._submeter():
                break
        
        if self._ao_concluir:
            self._ao_concluir()
        
        return self._dados

    def get_dados(self) -> dict:
        return self._dados