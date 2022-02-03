pergunta = {
    'Perfil 1': {
        'tipo': 'Sou um objeto',
        'dicas': {
            '1': 'Tenho várias marcas.',
            '2': 'Sou usado pra trabalho e também pra diversão.',
            '3': 'Uso energia elétrica.',
            '4': 'Tenho teclas.',
            '5': 'Tenho mouse.',
            '6': 'Tenho monitor.',
        },
        'resposta': 'computador'
    },
    'Perfil 2': {
        'tipo': 'Sou um animal',
        'dicas': {
            '1': 'Gosto da noite.',
            '2': 'Me alimento de ratos.',
            '3': 'Sei voar, mas não vôo tanto.',
            '4': 'Minha visão é muito boa.',
            '5': 'Sou muito bela.',
        },
        'resposta': 'coruja'
    },
    'Perfil 3': {
        'tipo': 'Sou um objeto',
        'dicas': {
            '1': 'Registro momentos na minha memória.',
            '2': 'Posso iluminar o ambiente.',
            '3': 'Sou muito antiga.',
            '4': 'Passei por várias fases na minha vida.',
            '5': 'Hoje sou mais acessível, mas no passado era difícil de me usar.',
            '6': 'Já fui analógica e agora sou digital.'
        },
        'resposta': 'máquina fotográfica'
    },
    'Perfil 4': {
        'tipo': 'Sou um personagem',
        'dicas': {
            '1': 'Não gosto do dia.',
            '2': 'Dizem que me transformo em um ser voador.',
            '3': 'Não gosto de comidas com muito alho.',
            '4': 'Gosto de sangue.',
            '5': 'Durmo em um caixão.',
            '6': 'Uma estaca de madeira pode me matar.'
        },
        'resposta': 'vampiro'
    },
}

for chave_pergunta, valores_pergunta in pergunta.items():

    print(f'{chave_pergunta}: {valores_pergunta["tipo"]}')
    quantidade_dicas = len(valores_pergunta['dicas'].items())
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
        elif resposta_usuario not in valores_pergunta['dicas'].keys():
            print('ATENÇÃO - Não há dicas com esse número.')
        else:
            for chave_secundaria, valores_secundario in valores_pergunta['dicas'].items():
                if resposta_usuario == chave_secundaria:
                    print(f'{chave_secundaria}: {valores_secundario}')

                    if dicas_obtidas == '':
                        dicas_obtidas = resposta_usuario
                    elif resposta_usuario not in dicas_obtidas:
                        dicas_obtidas = dicas_obtidas + ',' + resposta_usuario

        print()