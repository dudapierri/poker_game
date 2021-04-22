class Carta:
    def __init__(self, posicao, valor, naipe):
        self.posicao = posicao
        self.valor = valor
        self.naipe = naipe

    def maiorQue(self, carta):
        return self.posicao > carta.posicao

    def print(self):
        print(self.valor+self.naipe)

class AvaliadorDeMao:
    def verificaRoyalFlush(mao):
        cartas = set()
        for i in mao:
            cartas.append(str(mao.valor) + mao.naipe)

        royalFlush1 = set(["10D", "VD", "DD", "RD", "AD"])
        royalFlush2 = set(["10H", "VH", "DH", "RH", "AH"])
        royalFlush3 = set(["10S", "VS", "DS", "RS", "AS"])
        royalFlush4 = set(["10C", "VC", "DC", "RC", "AC"])
        if ((royalFlush1 <= cartas) or (royalFlush2 <= cartas) or (royalFlush3 <= cartas) or (royalFlush4 <= cartas)):
            return True
        else:
            return False

def gerarMao(lista_cartas, lista_naipes):
    mao = []
    for i in range(5):
        indice = random.randint(len(lista_cartas))
        valor = Carta(
            indice,
            lista_cartas[indice],
            random.choice(lista_naipes)
        )
        mao.append(valor)
    return mao
import random
avaliador = AvaliadorDeMao()
lista_cartas = [2,3,4,5,6,7,8,9,10,"V", "D", "R", "A"]
lista_naipes = ["D", "H", "S", "C"]
partida = True
jogador1 = []
jogador2 = []


#while (partida == True):
contadorJogador1 = 0
contadorJogador2 = 0
jogador1 = gerarMao(lista_cartas, lista_naipes)
jogador2 = gerarMao(lista_cartas, lista_naipes)
print("mão jogador 1: " + jogador1)
print("mão jogador 2: " + jogador2)
if (avaliador.verificaRoyalFlush(jogador1)):
    print("jogador 1 : Royal Flush")
    print("Vencedor: jogador1!")
if (avaliador.verificaRoyalFlush(jogador2)):
    print("jogador 2 : Royal Flush")
    print("Vencedor: jogador2!")
