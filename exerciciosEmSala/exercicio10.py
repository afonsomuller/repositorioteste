from random import shuffle
lista_alfanum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
shuffle(lista_alfanum)
captcha_lista = []
for caracter in range(0,6):
    captcha_lista.append(lista_alfanum[caracter])
captcha = ''.join(captcha_lista)
print(captcha)
print('Digite abaixo o mesmo que você ve no captcha:')
compara_captcha = str(input(''))
if compara_captcha == captcha:
    print('Tudo Certo, pode navegar!')
else:
    print('Vai aonde, robô?')