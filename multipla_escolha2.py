perguntas = {
    'Pergunta 1': {
        'pergunta': 'Qual o super-herói é laranja?',
        'resposta': {'a': 'Hulk', 'b': 'Coisa', 'c': 'Fera'},
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Qual a super-heroína que tem um jato invisível?',
        'resposta': {'a': 'Mulher maravilha', 'b': 'Mulher invisível', 'c': 'Vampira'},
        'resposta_certa': 'a'
    },
    'Pergunta 3': {
        'pergunta': 'Qual o super herói que não consegue voar?',
        'resposta': {'a': 'Magneto', 'b': 'Homem de Ferro', 'c': 'Hulk'},
        'resposta_certa': 'c'
    },
    'Pergunta 4': {
        'pergunta': 'Qual o super herói que não é baseado em um animal?',
        'resposta': {'a': 'Wolverine', 'b': 'Homem de gelo', 'c': 'Homem aranha'},
        'resposta_certa': 'b'
    },
    'Pergunta 5': {
        'pergunta': 'Qual o super herói não trabalha em um jornal?',
        'resposta': {'a': 'Homem de gelo', 'b': 'Homem aranha', 'c': 'Super homem'},
        'resposta_certa': 'a'
    },
    'Pergunta 6': {
        'pergunta': 'Qual o super herói consegue voltar à forma humana?',
        'resposta': {'a': 'Coisa', 'b': 'Fera', 'c': 'Colossus'},
        'resposta_certa': 'c'
    },
    'Pergunta 7': {
        'pergunta': 'Qual o super herói que tem super poderes?',
        'resposta': {'a': 'Arqueiro verde', 'b': 'Batman', 'c': 'Tocha humana'},
        'resposta_certa': 'c'
    },
}

respostas_corretas = 0

for chave_pergunta, valores_pergunta in perguntas.items():
    print(f'{chave_pergunta}: {valores_pergunta["pergunta"]}')

    for chave_resposta, valores_resposta in valores_pergunta['resposta'].items():
        print(f'[{chave_resposta}]: {valores_resposta}')

    resposta_usuario = input("Digite a sua resposta:")
    if resposta_usuario == valores_pergunta["resposta_certa"]:
        print('Você acertou!')
        respostas_corretas += 1
    else:
        print('Você errou!')

    print()

porcentagem_acerto = (respostas_corretas / len(perguntas)) * 100
print(f'Você acertou {respostas_corretas} respostas. {porcentagem_acerto:.1f}% de acerto')