perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2',
        'resposta': {'a': '1', 'b': '4', 'c': '5', },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2',
        'resposta': {'a': '4', 'b': '10', 'c': '6', },
        'resposta_certa': 'c',
    },
}

respostas_corretas = 0

for chave_pergunta, valores_pergunta in perguntas.items():
    print(f'{chave_pergunta}: {valores_pergunta["pergunta"]}')

    print("Respostas: ")
    for chave_resposta, valores_resposta in valores_pergunta['resposta'].items():
        print(f'[{chave_resposta}]: {valores_resposta}')

    #print(f'{valores_pergunta["resposta_certa"]}')
    resposta_usuario = input('Sua resposta:')

    if resposta_usuario == valores_pergunta['resposta_certa']:
        print('Acertou')
        respostas_corretas +=1
    else:
        print('Errou')

    print()

    quantidade_perguntas = len(perguntas)
    porcentagem_acerto = (respostas_corretas / quantidade_perguntas) * 100

    print(f'Você acertou {porcentagem_acerto}% das perguntas.')