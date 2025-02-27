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

def opcao_invalida():
    print("Opção inválida.")
    input("digite outro número para voltar ao menu principal.")
    main()

def escolhendo_opcao():
    try:
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
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opçoes()
    escolhendo_opcao()

if __name__ == "__main__":
    main()