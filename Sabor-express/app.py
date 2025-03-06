import os

restaurantes = [{"nome": "McDonald's", "categoria": "fast food", "ativo": False},
                {"nome": "GoCoffee", "categoria": "café", "ativo": True},
                {"nome": "BubbleMix", "categoria": "Chá de bolhas", "ativo": False},]

def exibir_nome_do_programa():
    '''Exibe o nome do programa.
    
    Outputs:
    nome do programa
    '''
    print("𝓢𝓪𝓫𝓸𝓻 𝓮𝔁𝓹𝓻𝓮𝓼𝓼\n")

def exibir_opçoes():
    '''Exibe as opções disponíveis.
    
    Outputs:
    Opções
    '''
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def finalizando_programa():
    '''Finaliza o programa.
    
    Outputs:
    Mensagem de finalização do programa.
    '''
    os.system("cls")
    # os.clear("clear") em computadores mac
    print("Encerrando programa\n")

def voltar_ao_menu_principal():
    '''Volta ao menu principal após encerrar as operações em uma opção.
    
    Input:
    Tecla Aleatória

    Output:
    Menu principal
    '''
    input("Digite uma tecla para coltar ao menu principal. ")
    main()

def opcao_invalida():
    '''Indica quando uma opção escolhida não é correspondida e retorna ao menu principal.
    
    Output:
    Menu principal
    '''
    print("Opção inválida.")
    voltar_ao_menu_principal()

def inicio_da_funcao(texto):
    '''Limpa o terminal e mostra o subtítulo.
    
    Output:
    Linhas iniciais da função
    '''
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Coleta os dados de um novo restaurante o colocaos no dicionário.
    
    Input:
    Nome do Restaurante
    Categoria do restaurante

    Output:
    Adiciona novo restaurante na lista
    '''
    inicio_da_funcao("Cadastro de novos restaurantes")
    nome_do_restaurante = str(input("Digite o nome do restaurante que deseja cadastrar: "))
    categoria = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Mostra os restaurantes cadastrados, suas categorias e estado.
    
    Output:
    Lista de restaurantes
    '''
    inicio_da_funcao("Listando restaurantes")
    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Estado")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        tipo_restaurante = restaurante["categoria"]
        ativado = "Ativado" if restaurante["ativo"] else "Desativado"
        print(f"->{nome_restaurante.ljust(20)} | {tipo_restaurante.ljust(20)} | {ativado}\n")
    voltar_ao_menu_principal()

def alterando_estado_restaurante():
    '''Altera o estado dos restaurantes cadastrados.
    
    Input:
    Nome do restaurante que se deseja mudar o estado

    Output:
    Mudança de estado do restaurante
    '''
    inicio_da_funcao("Alternando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            print(mensagem)
        
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado.")

    voltar_ao_menu_principal()

def escolhendo_opcao():
    '''Chama as funções de acordo com a opção escolhida.
    
    Input:
    Número da função escolhida

    Output:
    Função escolhida
    '''
    try:
        opção_escolhida = int(input("Escolha uma opção: "))
        match opção_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterando_estado_restaurante()
            case 4:
                finalizando_programa()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("cls")
    '''Chama o menu principal'''
    exibir_nome_do_programa()
    exibir_opçoes()
    escolhendo_opcao()

if __name__ == "__main__":
    main()