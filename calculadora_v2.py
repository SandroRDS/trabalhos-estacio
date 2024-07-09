saida = ''

def adicao(operando1, operando2):
    return operando1 + operando2

def subtracao(operando1, operando2):
    return operando1 - operando2

def multiplicacao(operando1, operando2):
    return operando1 * operando2

def divisao(operando1, operando2):
    if (operando1 == 0 or operando2 == 0): return 'Não foi possível realizar a divisão por 0'
    return  operando1 / operando2

def calculadora(operando1, operando2, operacao):
    resultado = ''

    match(operacao):
        case '+':
            resultado = adicao(operando1, operando2)
        case '-':
            resultado = subtracao(operando1, operando2)
        case '*':
            resultado = multiplicacao(operando1, operando2)
        case '/':
            resultado = divisao(operando1, operando2)

    return resultado

while (str.lower(saida) != 'n'):
    operando1 = int(input('Insira o primeiro operando: '))
    operando2 = int(input('Insira o segundo operando: '))
    operacao = input('Insira o sinal da operação: ')

    resultado = calculadora(operando1, operando2, operacao)
    print(f'Resultado da operação: {resultado}')
    saida = input('Deseja realizar uma nova operação ? (S/N)')
