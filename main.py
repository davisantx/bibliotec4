from data.db import inicializar_banco
from ui.componentes import menu_inicial
from ui.montador import configurar_menus


def main() -> None:
    inicializar_banco()
    configurar_menus()
    menu_inicial.exibir()

if __name__ == "__main__":
    main()