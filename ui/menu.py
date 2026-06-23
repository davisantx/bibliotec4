from abc import ABC, abstractmethod

from ui.estados import Estado


class IO(ABC):
    """
    Classe abstrata herdada pelos componentes Menu e Formulário.
    """

    def __init__(self):
        self._titulo = "MENU"

    @abstractmethod
    def exibir(self) -> Estado:
        """
        Função responsável pela exibição dos Menus e Formulários
        """
        pass


class Menu(IO):
    def __init__(self, titulo: str):
        self._titulo = titulo
        self._opcoes = []
        self._saida = None
        self._opcao_selecionada = ""
        self.add_navegacao("Sair", self.sair)

    def sair(self):
        print("Saindo do sistema...")
        exit()

    def add_opcao(self, texto: str, acao=None) -> "Menu":
        """
        Função destinada a adicionar uma opção ao Menu

        Uma opção é formada por uma tupla (atalho: int, texto: str, acao: função)
        """

        opcoes_normais = [opcao for opcao in self._opcoes if opcao[0] != 0]
        self._opcoes.append((len(opcoes_normais) + 1, texto, acao))
        return self

    def add_navegacao(self, texto: str, acao=None):
        """
        Função destinada a adicionar uma opção de navegação ao Menu

        Por padrão, o atalho é sempre 0

        E nunca há mais de uma opção de navegação ao mesmo tempo
        """

        self._opcoes = [opcao for opcao in self._opcoes if opcao[0] != 0]
        self._opcoes.insert(0, (0, texto, acao))
        return self

    def limpar_opcoes(self) -> "Menu":
        """
        Função destinada a retirar todas as opções, com exceção da opção de navegação.
        """

        self._opcoes = [opcao for opcao in self._opcoes if opcao[0] == 0]
        return self

    def _formatar_menu_para_exibicao(self) -> str:
        saida = f"\n{self._titulo.upper()}\n"

        for atalho, texto, _ in self._opcoes:
            if atalho != 0:
                saida += f"{atalho}. {texto}\n"

        sair_atalho, sair_texto, _ = self._opcoes[0]
        saida += f"{sair_atalho}. {sair_texto}\n"

        return saida

    def formatar_valor_input(self, valor_input: str) -> str:
        """
        Função destinada a formatar a string inserida no input.\n
        Se inserido a opção: 

        ```
          1      2
        ```
        A função vai retornar:
        ```
        "12"
        ```
        """
        return "".join(valor_input.split())

    def exibir(self) -> Estado:
        """
        Função destinada a exibir o Menu, com seu título e opções

        Para além disso, controla o fluxo de execução considerando a função _processar()

        Quando _processar() retornar uma str ou None o Menu é reexibido

        Se o retorno for o item da enum: Sinal.CONTINUAR, o mesmo Menu não é reexibido
        """

        while True:
            print(self._formatar_menu_para_exibicao())

            estado = self._processar()

            if estado is not Estado.RECARREGAR:
                return estado

    def _capturar_campos(self) -> Estado | int:
        try:
            print("-" * 40)
            escolha = int(self.formatar_valor_input(input("Escolha: ").strip()))
            print(f"{'-' * 40}\n")
            return escolha
        except ValueError:
            print("\nErro! Opção inválida: Insira um número!")
            return Estado.RECARREGAR
            
    def _processar(self) -> Estado:
        """
        Função destinada a:
        1. Receber a entrada do usuário, repetindo-a caso ocorra uma exceção ValueError

        1. Percorrer as opções
        2. Se chegar na opção de escolha, ele verifica se o valor do atalho é 0
        3. Se for 0, retorna None e repete volta pro Menu anterior
        """

        escolha: Estado | int = self._capturar_campos()

        if escolha is Estado.RECARREGAR:
            return escolha

        for atalho, texto, acao in self._opcoes:
            if escolha == atalho:
                if atalho == 0:
                    if acao:
                        acao()
                    return Estado.CANCELADO
                if acao:
                    acao()
                    return Estado.RECARREGAR

                # Salva o texto da opção selecionada
                # É verificado na função de input personalizado exibir_autor()
                self._opcao_selecionada = texto
                return Estado.SUCESSO

        print("\nErro! Opção inválida: Opção selecionada não existe.")
        return Estado.RECARREGAR

    def get_opcao_selecionada(self) -> str:
        return self._opcao_selecionada


class Formulario(IO):
    """
    O formulário tem como objetivo:

    1. Exibir o título
    2. Exibir os campos
    3. Receber dados nesses campos
    4. Validar há dados nesses campos
    5. Executar uma ação após a submissão dos dados no formulário, se houver:
            - _acao_ao_confirmar_submissao
    6. Executar uma última ação, se houver:
            - _acao_ao_concluir
    """

    def __init__(self, titulo: str):
        self._titulo: str = titulo
        self._campos: list[tuple] = []
        self._dados: dict = {}
        self._acao_ao_confirmar_submissao = None
        self._acao_ao_concluir = None

    def ao_concluir(self, acao) -> "Formulario":
        """
        Função destinada a receber a função ao_concluir, que é executada
        """

        self._ao_concluir = acao
        return self

    def ao_confirmar_submissao(self, acao) -> "Formulario":
        """
        Função destinada a receber a função ao_submeter, executada quando todos os campos
        de input do formulário são inseridos.
        """

        self._acao_ao_confirmar_submissao = acao
        return self

    def add_campo(
        self, chave: str, nome_campo: str, input_personalizado=None, tipo_da_entrada=str
    ) -> "Formulario":

        def input_padrao():
            print("-" * 60) 
            saida = input(f"{nome_campo}: ") 
            print("-" * 60)
            return saida
            
        input_campo = input_padrao
        
        if input_personalizado:
            input_campo = input_personalizado

        campo = (chave, nome_campo, input_campo, tipo_da_entrada)

        self._campos.append(campo)

        return self

    def _exibir_titulo(self) -> None:
        """
        Funcão destinada a exibir o título.
        """
        titulo = f"\n{self._titulo.upper()}"
        titulo += "\n(Digite 0 para voltar)\n"
        print(titulo)

    def verificar_se_input_e_vazio(self, valor_input_formatado: str) -> bool:
        """
        Função destinada a verificar se o input está vázio.
        """
        input_e_vazio = len(valor_input_formatado) == 0
        if input_e_vazio:
            print(
                "\nErro! Campo vázio: \nSelecione a opção novamente e insira um valor."
            )
        return input_e_vazio

    def formatar_valor_input(self, valor_input: str) -> str:
        """
        Função destinada a formatar a string inserida no input.\n
        Retorna a string formatada.
        """
        return " ".join(valor_input.split())

    def _capturar_campos(self) -> bool:
        """
        Função destinada a capturar valores de entrada de cada campo

        Se o valor inserido for 0, volta para o Menu anterior

        Se o valor inserido for diferente disso
        """

        self._dados = {}
        for chave, _, input_campo, tipo_de_entrada in self._campos:
            
            valor_recebido = input_campo()
            
            valor = self.formatar_valor_input(valor_recebido)
   
            if self.verificar_se_input_e_vazio(valor):
                return False

            if tipo_de_entrada is int:
                try:
                    valor = int(valor)
                except ValueError:
                    print("Valor inválido de ID! Insira um número!")
                    return False

            # Se o usuário digitar 0 no campo do formulário ele volta para o Menu anterior
            if tipo_de_entrada is int and valor == 0:
                return False

            if tipo_de_entrada is str and valor == "0":
                return False

            self._dados[chave] = str(valor)

        
        return True

    def _executar_a_acao_de_submissao(self) -> bool:
        """
        Função destinada a executar a ação de submissão do formulário

        Quando sucesso, retorna True e sai do formulário
        Quando falha, retorna False e reexibe o formulário
        """

        # Verifica se não é None
        if self._acao_ao_confirmar_submissao:
            resultado = self._acao_ao_confirmar_submissao(self._dados)

            if resultado is False:
                return False
            return True

        """
        Se o formulário não tem ação após a submissão do formulário, retorna True,
        devolvendo apenas os dados inseridos
        """
        return True

    def exibir(self) -> Estado:
        """
        Se retornar Estado.CANCELADO, volta pra exibição do Menu anterior (quando usuário digitar 0).
            - Quando o usuário insere o 0 para sair do sistema, ele executa a ação de sair do sistema e ainda retorna Estado.CANCELADO
            - Se retornar Estado.SUCESSO, o formulário foi concluído com sucesso

        """

        self._exibir_titulo()

        if not self._capturar_campos():
            return Estado.CANCELADO

        self._executar_a_acao_de_submissao()

        if self._acao_ao_concluir:
            self._acao_ao_concluir()

        return Estado.SUCESSO

    def get_dados(self) -> dict:
        return self._dados
