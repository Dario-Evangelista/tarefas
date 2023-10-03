import json

def add_tarefas():
    try:
        with open('data.json', 'r') as arquivos:
            tarefas = json.load(arquivos)
    except FileNotFoundError:
        tarefas = []

    while True:

        tarefa = input(f"Qual seria a tarefa? \n")
        dia = input(f"Dia: ")
        mes = input(f"Mês: ")
        ano = input(f"Ano: ")

        dados = {
            "tarefa": tarefa,
            "dia": dia,
            "mes": mes,
            "ano": ano
        }

        tarefas.append(dados)
        print(tarefas)

        continuar = input('Deseja adicionar mais tarefas? (s/n): ')
        if continuar.lower() != 's':
            break

    with open('data.json', 'w') as arquivos:
        json.dump(tarefas, arquivos, indent=1)

    menu()

def apagar():
    try:
        with open('data.json', 'r') as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []
        print("Você não tem tarefas salvas.")
        return
    
    for tarefa in tarefas:
        print(tarefa)

    tarefa_para_remover = input("Digite a tarefa que deseja remover: ")
    tarefas = [tarefa for tarefa in tarefas if tarefa.get('tarefa') != tarefa_para_remover]

    with open('data.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=1)

    print(f'Tarefa com nome "{tarefa_para_remover}" removida do JSON.')

    menu()

def feito():
    try:
        with open('data.json', 'r') as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []
        print("Você não tem tarefas salvas.")
        return
    
    try:
        with open('feito.json', 'r') as arquivo:
            concluido = json.load(arquivo)
    except FileNotFoundError:
        concluido = []

    print(tarefas)
    for concluidos in concluido:
        print(f"Concluidos: {concluidos}")

    while True:
        feito = input(f'Qual tarefa você concluiu? ')

        tarefa_encontrada = None
        for tarefa in tarefas:
            if tarefa.get('tarefa') == feito:
                tarefa_encontrada = tarefa
                break

        if tarefa_encontrada:
            concluido.append(tarefa_encontrada)
            tarefas.remove(tarefa_encontrada)
        else:
            print('Não existe essa tarefa.')

        print('Tarefas concluídas:')
        for item in concluido:
            print(item['tarefa'])

        continuar = input('Deseja adicionar mais tarefas concluídas? (s/n): ')
        if continuar.lower() != 's':
            break
    
    with open('data.json', 'w') as arquivos:
        json.dump(tarefas, arquivos, indent=1)

    with open('feito.json', 'w') as arquivos:
        json.dump(concluido, arquivos, indent=1)
    menu()
        
def menu():
    print(f"Escolha uma opção\n\n")
    print(f"1-Adicionar uma tarefa\n")
    print(f"2-Remover uma tarefa\n")
    print(f"3-Concluir uma tarefa\n")
    print(f"0-exit\n")
    opcao = input(f"Escolha um numero: ")

    if opcao == '1':
        add_tarefas()

    elif opcao == '2':
        apagar()

    elif opcao == '3':
        feito()

    elif opcao == '0':
        print('exit')

    else:
        print('Opção invalida')

menu()
