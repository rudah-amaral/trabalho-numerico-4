from modules.trapezio import metodo_trapezio
from modules.simpson import metodo_simpson
from modules.comparacoes import comparar_metodos

def main():
    while True:
        print("Escolha o método de integração:\n1. Método do Trapézio\n2. Método de Simpson\n3. Comparar métodos\n-1. Sair")

        escolha = input("Digite o número da opção desejada: ")
        if escolha == "-1":
            print("Saindo do programa.")
            break
        switcher = {
            "1": metodo_trapezio,
            "2": metodo_simpson,
            "3": comparar_metodos
        }
        funcao = switcher.get(escolha)
        if funcao:
            funcao()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.\n")

if __name__ == "__main__":
    try:
        main()   # o que você já executa hoje
    except Exception as e:
        print(f"\nErro: {e}")
    input("\nPressione Enter para sair...")