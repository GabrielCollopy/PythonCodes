listaTarefas = []
def exibirMenu():
    print("Menu: ")
    print("1. Adicionar nova tarefa")
    print("2. Exibir tarefas")
    print("3. Sair")

def adicionarTarefa(listaTarefas):
    listaTarefas = []
    tarefa = (str(input("Qual tarefa deseja adicionar? ")))
    print("Digite sair quando terminar de adicionar")
    while (tarefa != "sair"):
        listaTarefas.append(tarefa)
        tarefa = (str(input("Qual tarefa deseja adicionar? ")))
    print("Nova terefa adicionada!")

def exibirTarefas():
    #codigo para exibir as tarefas existentes
    print("Tarefas existentes: ")
    print("- Tarefa 1")
    print("- Tarefa 2")

def principal():
    while True:
        exibirMenu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionarTarefa(listaTarefas)
        elif opcao == "2":
            exibirTarefas()
        elif opcao == "3":
            exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    principal()


