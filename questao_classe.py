# Implemente uma classe ListaTarefas que gerencie uma lista simples de tarefas a fazer.

# Sua classe deve ter os seguintes métodos:
# adicionar(tarefa) - Adiciona uma nova tarefa ao final da lista
# remover(tarefa) - Remove uma tarefa específica da lista
# listar() - Retorna todas as tarefas
# marcar_concluida(tarefa) - Marca uma tarefa como concluída (adicione "finalizada" ao final)
# total() - Retorna o número total de tarefas

class ListaTarefas:
    def __init__(self):
        self.lista = []

    def adicionar(self, tarefa):
        self.lista.append(tarefa)
        print("Tarefa adicionada ao final da lista!")

    def remover(self, tarefa):
        if tarefa in self.lista:
            self.lista.remove(tarefa)
            print("Removido a tarefa com sucesso!")
        else:
            print("Tarefa não encontrada!")

    def listar(self):
        if (len(self.lista) == 0):
            print("Nenhuma tarefa para listar!")
            return
        for i in self.lista:
            print(i)

    def marcar_concluida(self, tarefa):
        for i in range(len(self.lista)):
            if (self.lista[i] == tarefa):
                self.lista[i] = self.lista[i] + " - Finalizada"
                print("Tarefa finalizada com sucesso!")
                return
        print("Tarefa não encontrada!")

    def total(self):
        return len(self.lista)

solucao = ListaTarefas()

def teste():
    solucao.adicionar("Tarefa 1")
    solucao.adicionar("Tarefa 2")
    solucao.listar()
    solucao.marcar_concluida("Tarefa 1")
    solucao.listar()
    solucao.remover("Tarefa 4")
    solucao.remover("Tarefa 2")
    solucao.listar()
    print("Total de tarefas:", solucao.total())

teste()