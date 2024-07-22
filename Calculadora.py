import sys

class Calculadora:
    simbolosAceitos = ['+', '-', '*', '/']

    def __init__(self):
        self.__valorA = float(input('Primeiro termo: '))
        self.__valorB = float(input('Segundo termo: '))
        self.__operacao = input('Operação: ')

    @property
    def valorA(self):
        return self.__valorA

    @valorA.setter
    def valorA(self, valorA):
        self.__valorA = valorA

    @property
    def valorB(self):
        return self.__valorB

    @valorB.setter
    def valorB(self, valorB):
        self.__valorB = valorB

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    def validarOperacao(self, simbolo):
        return simbolo in self.simbolosAceitos

    def calcular(self):
        if (not self.validarOperacao(self.__operacao)):
            print('Operação Inválida')
            sys.exit(0)

        match(self.operacao):
            case '+':
                return self.valorA + self.valorB
            case '-':
                return self.valorA - self.valorB
            case '*':
                return self.valorA * self.valorB
            case '/':
                if (self.valorA == 0 or self.valorB == 0):
                    print('Um dos termos não pode ser 0')
                    sys.exit(0)

                return self.valorA / self.valorB

    def mostrarResultado(self):
        print(str(self.valorA) + ' ' + self.operacao + ' ' + str(self.valorB) + ' = ' + str(self.calcular()))