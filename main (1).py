# =========================
# main.py
# =========================

from produtos import cadastrar_produto, listar_produtos
from estoque import entrada_estoque, saida_estoque
from vendas import registrar_venda


def menu():
    while True:
        print("\n===== CONTROLE DE ESTOQUE =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Entrada de estoque")
        print("4 - Saída de estoque")
        print("5 - Registrar venda")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            entrada_estoque()

        elif opcao == "4":
            saida_estoque()

        elif opcao == "5":
            registrar_venda()

        elif opcao == '6':
            relatorio_estoque()

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


menu()
