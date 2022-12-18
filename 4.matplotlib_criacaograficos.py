# Final do RU é 500 - alterado para 533

from matplotlib import pyplot as plt

# o menu irá trabalhar nos valores de y1,y2 e y3, pela equação ax+bx-c
def menu(x, a, b, c):
    y = a * x + b * x - c
    return y

x1 = 5   #valores de x
x2 = 7
x3 = 9

a = 5    #valores de a,b,c. Conforme o meu RU 500 = 533
b = 3
c = 3
plt.title('GRÁFICO DA LETÍCIA')  #inserindo o titulo
plt.grid()
plt.xlabel('EIXO LETÍCIA X') #inserindo o titulo do eixo x
plt.ylabel('EIXO LETÍCIA Y')  #inserindo o titulo do eixo y

plt.plot(x1, menu(x1, a, b, c), marker="o", markersize=18, markerfacecolor='green')
plt.plot(x2, menu(x2, a, b, c), marker="o", markersize=18, markerfacecolor='pink')
plt.plot(x3, menu(x3, a, b, c), marker="o", markersize=18, markerfacecolor='purple')
plt.show()

# class conta:
# def __init__(self, x):
#     self.x = int(x)
#
# def valor(self, x1, x2, x3):
#     a = 5
#     b = 3
#     c = 3
#     y = self.x * a + self.x * b - c
#     return y
# eixoX = [5, 7, 9]
# eixoY = []
# for i in eixoY:
#     y = conta(i)
#     eixoY.append(y.valor())
#     plt.plot(eixoX, eixoY, color='red')
#     plt.title('GRÁFICO DA LETÍCIA')
#     plt.eixoXlabel('EIXO LETÍCIA X')
#     plt.eixoYlabel('EIXO LETÍCIA Y')
#     plt.show()

# class conta:
#     def __init__(self):
#         self.x1 = 5
#         self.x2 = 7
#         self.x3 = 9
#         self.resultado = 0
#
#     def __init__(self):
#         self.a = 5
#         self.b = 3
#         self.c = 3
#         self.resultado = 0
#
#     def conta(self, x1, a, b, c):
#         self.x1 = x1
#         self.a = a
#         self.b = b
#         self.c = c
#         self.resultado = (self.a * self.x1) + (self.b * self.x1) - self.c
#         return self.resultado
#
#     print(conta)


# x = [5, 7, 9]
# y = [37, 53, 69]
#
# plt.plot(x, y)
# plt.plot(x, y, label='dados', color='#18821F', ls='--', lw='2')
# plt.legend(loc=20, fontsize=20)
# plt.xlabel('EIXO LETÍCIA X')
# plt.ylabel('EIXO LETÍCIA Y')
# plt.title('GRÁFICO DA LETÍCIA')
# plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
# plt.legend()
# plt.show()
