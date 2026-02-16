import os
import time
questoes = [
    { 
     'Pergunta':'Qual ano foi proclamado a Republica do Brasil?',
     'Opcoes': ['1850' , '1902', '1927', '1889'],
     'Resposta': '4'
    },
    {
    'Pergunta': 'Porque microondas existe?',
    'Opcoes': ['Esquentar' , 'Resfriar' , 'Desintegrar'],
    'Resposta': '1'
    }
]
def Quiz():
    contador = 0
    for i , o in enumerate(questoes):
        
        while True:
            print(f'\n{i+1}° Questao: {o["Pergunta"]}')
            for id , op in enumerate(o['Opcoes']):
                print(f'{id+1}- {op}')
            resposta = input('\nSua resposta: ')

            if not resposta.isdigit():
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Digite apenas o numero da resposta desejada!!!')
                print(('-')* 100)
                continue
            if int(resposta) > len(o['Opcoes']) or int(resposta) <= 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Opçao escolhida NAO existe')
                print(('-')* 100)
                continue
            if str(resposta) == o['Resposta']:
                print('Voce acertou!!')
                print(('-')* 100)
                contador += 1
            else:
                print(f'Voce errou, resposta certa era {o["Resposta"]} !!')
                print(('-')* 100)
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    print(f'Parabens voce acertou: {contador}/{len(questoes)}')

Quiz()
