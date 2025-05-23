cores = {
    'normal':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'roxo':'\033[34m',
    'magenta':'\033[35m',
    'ciano':'\033[36m',
    'cinza':'\033[37m'
}

estilo = {
     'normal':'\033[0;30m',
     'negrito':'\033[1;30m',
     'sublinhado':'\033[4;30m',
     'negativo':'\033[7;30m',
 }

fundo = {
     'normal':'\033[;;40m',
     'vermelho':'\033[;;41m',
     'verde':'\033[0;0;47m',
     'amarelo':'\033[;;43m',
     'roxo':'\033[;;44m',
     'magenta':'\033[;;45m',
     'ciano':'\033[;;46m',
     'cinza':'\033[;;47m',
 }


if __name__ == "__main__":

    print('\nTexte dos cores do texto:   {}vermelho{}'.format(cores['vermelho'], cores['normal']))
    print('Texte dos cores do texto:   {}verde{}'.format(cores['verde'], cores['normal']))
    print('Texte dos cores do texto:   {}amarelo{}'.format(cores['amarelo'], cores['normal']))
    print('Texte dos cores do texto:   {}roxo{}'.format(cores['roxo'], cores['normal']))
    print('Texte dos cores do texto:   {}magenta{}'.format(cores['magenta'], cores['normal']))
    print('Texte dos cores do texto:   {}ciano{}'.format(cores['ciano'], cores['normal']))
    print('Texte dos cores do texto:   {}cinza{}\n'.format(cores['cinza'], cores['normal']))

    print('\nTexte dos estilos:   {}negrito{}'.format(estilo['negrito'], cores['normal']))
    print('Texte dos estilos:   {}sublinhado{}'.format(estilo['sublinhado'], cores['normal']))
    print('Texte dos estilos:   {}negativo{}'.format(estilo['negativo'], cores['normal']))

    print('\nTexte de cores de fundo:   {}vermelho{}'.format(fundo['vermelho'], cores['normal']))
    print('Texte de cores de fundo:   {}verde{}'.format(fundo['verde'], cores['normal']))
    print('Texte de cores de fundo:   {}amarelo{}'.format(fundo['amarelo'], cores['normal']))
    print('Texte de cores de fundo:   {}roxo{}'.format(fundo['roxo'], cores['normal']))
    print('Texte de cores de fundo:   {}magenta{}'.format(fundo['magenta'], cores['normal']))
    print('Texte de cores de fundo:   {}ciano{}'.format(fundo['ciano'], cores['normal']))
    print('Texte de cores de fundo:   {}cinza{}\n'.format(fundo['cinza'], cores['normal']))
