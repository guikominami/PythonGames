pergunta = {
    'Perfil 1': {
        'tipo': 'Sou um objeto',
        'dicas': [
            'Tenho várias marcas.',
            'Sou usado pra trabalho e também pra diversão.',
            'Uso energia elétrica.',
            'Tenho teclas.',
            'Tenho mouse.',
            'Tenho monitor.'
        ],
        'resposta': 'computador'
    },
    'Perfil 2': {
        'tipo': 'Sou um animal',
        'dicas': [
            'Gosto da noite.',
            'Me alimento de ratos.',
            'Sei voar, mas não vôo tanto.',
            'Minha visão é muito boa.',
            'Sou muito bela.'
        ],
        'resposta': 'coruja'
    },
    'Perfil 3': {
        'tipo': 'Sou um objeto',
        'dicas': [
            'Registro momentos na minha memória.',
            'Posso iluminar o ambiente.',
            'Sou muito antiga.',
            'Passei por várias fases na minha vida.',
            'Hoje sou mais acessível, mas no passado era difícil de me usar.',
            'Já fui analógica e agora sou digital.'
        ],
        'resposta': 'máquina fotográfica'
    },
    'Perfil 4': {
        'tipo': 'Sou um personagem',
        'dicas': [
            'Não gosto do dia.',
            'Dizem que me transformo em um ser voador.',
            'Não gosto de comidas com muito alho.',
            'Gosto de sangue.',
            'Durmo em um caixão.',
            'Uma estaca de madeira pode me matar.'
        ],
        'resposta': 'vampiro'
    },
}

for chave_pergunta, valores_pergunta in pergunta.items():

    print(f'{chave_pergunta}: {valores_pergunta["tipo"]}')
    quantidade_dicas = len(valores_pergunta['dicas'])
    dicas_obtidas = ''

    resposta = False
    while resposta == False:
        resposta_usuario = input(f'Digite um número de 1 a {quantidade_dicas} para '
                                 f'obter uma dica ou digite a resposta '
                                 f'(dicas obtidas: {dicas_obtidas}):')

        if resposta_usuario.isnumeric() == False and resposta_usuario.lower() == valores_pergunta['resposta']:
            print(f'Resposta CORRETA: {resposta_usuario}')
            resposta = True
        elif resposta_usuario.isnumeric() == False and resposta_usuario.lower() != valores_pergunta['resposta']:
            print(f'Resposta INCORRETA: {resposta_usuario}')
        elif int(resposta_usuario) > quantidade_dicas or int(resposta_usuario) == 0:
            print('ATENÇÃO - Não há dicas com esse número.')
        else:
            indice = int(resposta_usuario) - 1
            dica = valores_pergunta['dicas'][indice]
            print(f'{resposta_usuario}: {dica}')

            if dicas_obtidas == '':
                dicas_obtidas = resposta_usuario
            elif resposta_usuario not in dicas_obtidas:
                dicas_obtidas = dicas_obtidas + ',' + resposta_usuario

        print()