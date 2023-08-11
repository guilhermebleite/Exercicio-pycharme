if/else cadastro idade 
n=int(input('Digite o ano em que você nasceu:'))
idade = 2023-n
atraso= idade - 18
falta= 18-idade
if idade >= 18:
    print('Você precisa se alistar, pois você tem {} anos de idade'.format(idade))
    print('Passou {} anos que você precisaria se apresentar'.format(atraso))
else:
    print('Ainda não chegou seu momento. sua idade é: {} anos'.format(idade))
    print('faltam {} anos pra você se alistar'.format(falta))
    