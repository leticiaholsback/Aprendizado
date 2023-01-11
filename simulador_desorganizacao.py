import random
import seaborn as sns

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 50) if i % 2 == 0]  # halteres é um atributo e o i é uma lista
        # vai do halter 10 a 36kg, e if i % 2==0 esse código usado para o resto par, ou seja, apenas numeros pares
        self.porta_halteres = {}  # dicionario vazio
        self.reinicio_dia()
        # dicionario onde as chaves vao ter as posiçoes e os valores os hateres pegos, qdo pega um halter fica 0

    def reinicio_dia(self):  # essa funcao vai reorganizar os halteres
        self.porta_halteres = {i: i for i in
                               self.halteres}  # compreensao em dicionario, i: como chave e i como valor em cada i em self.halteres

    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]

    def listar_espacos(self):
        return [i for i, j in self.porta_halteres.items() if j == 0]

    def pegar_haltere(self, peso):
        posicao_haltere = list(self.porta_halteres.values()).index(
            peso)  # index pergunta qual o indice de um deter valor, retorna qual posicao esta a chave pedida
        chave_haltere = list(self.porta_halteres.keys())[posicao_haltere]
        self.porta_halteres[chave_haltere] = 0
        return peso

    def devolver_haltere(self, posicao, peso):
        self.porta_halteres[posicao] = peso

    def calcular_desordem(self):
        num_desordem = [i for i, j in self.porta_halteres.items() if i != j]
        return len(num_desordem) / len(self.porta_halteres)


class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo  # TIPO 1: NORMAL | TIPO 2: BAGUNCEIRO
        self.academia = academia
        self.peso = 0

    def inicio_treino(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = random.choice(lista_pesos)
        self.academia.pegar_haltere(self.peso)  # selecao aleatoria

    def fim_treino(self):
        espacos = self.academia.listar_halteres()
        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_haltere(self.peso, self.peso)  # pede posicao e peso
            else:  # se o peso nao eestiver disponivel sera colocado de forma aleatoria
                pos = random.choice(espacos)
                self.academia.devolver_haltere(pos, self.peso)
        if self.tipo == 2:  # o peso sempre sera colocado de forma aleatoria (TIPO BAGUNCEIRO)
            pos = random.choice(espacos)
            self.academia.devolver_haltere(pos, self.peso)
        self.peso = 0


academia = Academia()  # instancia da classe Academia

usuarios = [Usuario(1, academia) for i in range(10)]  # compreensao em lista fr 10 e todos sao do tipo 1 e self.academia vai ser um ponteiro (uma ref para a memoria) aponta para academia=Academia
usuarios += [Usuario(2, academia) for i in range(1)]  # += concatenar a lista com 1 usuario tipo 2
random.shuffle(usuarios)  # random.shuffle bagunca a lista

list_chaos = []

for k in range(50):
    academia.reinicio_dia()
    for i in range(10):  # aqui passa por 10 sessoes de treinos
        random.shuffle(usuarios)
        for user in usuarios:
            user.inicio_treino()
        for user in usuarios:
            user.fim_treino()
    list_caos += [academia.calcular_desordem()]


academia.porta_halteres
academia.calcular_desordem()

sns.displot(list_caos)

