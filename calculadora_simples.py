
# Calculadora simples

import os

def calculadora():

    operacoes = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }

    while True:

        print(
            '\nOperadores disponíveis:'
            '\n+ = soma'
            '\n- = subtração'
            '\n* = multiplicação'
            '\n/ = divisão'
            '\nFormato: 2+2\n'
        )

        calculo = input('Digite o cálculo: ').replace(' ', '')

        if not calculo:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Digite algo.')
            continue

        operador = None

        for op in operacoes:
            if op in calculo:
                operador = op
                break

        if operador is None:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Operador inválido.')
            continue

        try:

            parte1, parte2 = calculo.split(operador)

            numero1 = float(parte1)
            numero2 = float(parte2)

            resultado = operacoes[operador](numero1, numero2)

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'{calculo} = {resultado}')

            break

        except ValueError:
            print('Formato inválido. Ex: 10+10')

        except ZeroDivisionError:
            print('Não é possível dividir por zero.')

calculadora()

    

