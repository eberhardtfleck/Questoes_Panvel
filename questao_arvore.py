from collections import deque

class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children if children else []

def teste(root):
    if not root:
        return []

    resultado = []
    fila = deque([root])

    while fila:
        nivel = []
        tamanho = len(fila)

        for _ in range(tamanho):
            no = fila.popleft()
            nivel.append(no.val)
            
            for filho in no.children:
                fila.append(filho)

        resultado.append(nivel)

    return resultado

raiz = Node(1, [Node(10), Node(20, [Node(25), Node(35)]), Node(50)])
print(teste(raiz))