anacleto = 1.5
felisberto = 1.1
contador = 0
while anacleto >= felisberto:
    anacleto += 0.02
    felisberto += 0.03
    contador += 1
print('Passaram-se {} anos. Anacleto tem {:.2f}m de altura e Felisberto tem {:.2f}m de altura.'.format(contador, anacleto, felisberto))

