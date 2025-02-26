import os

def exibir_nome_do_programa():
    print("𝓢𝓪𝓫𝓸𝓻 𝓮𝔁𝓹𝓻𝓮𝓼𝓼\n")

def exibir_opçoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Validar restaurante")
    print("4. Sair\n")

def finalizando_programa():
    os.system("cls")
    # os.clear("clear") em computadores mac
    print("Encerrando programa\n")

def escolhendo_opcao():
    opção_escolhida = int(input("Escolha uma opção: "))
    match opção_escolhida:
        case 1:
            print("Cadastrar restaurante")
        case 2:
            print("Listar restaurantes")
        case 3:
            print("Validar restaurantes")
        case 4:
            finalizando_programa()
        case _:
            print("Opção inválida.")
    #    opcao_escolhida = int(input("Escolha uma opção: "))
    #    if opcao_escolhida == 1:
    #       print("Cadastrar restaurante")
    #    elif opcao_escolhida == 2:
    #       print("Listar restaurantes")
    #    elif opcao_escolhida == 3:
    #        print("Validar restaurante")
    #    else:
    #       finalizando_programa()

def main():
    exibir_nome_do_programa()
    exibir_opçoes()
    escolhendo_opcao()

if __name__ == "__main__":
    main()