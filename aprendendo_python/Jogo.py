import random


def pular_linha():
    print('')

vida_inimigo = 10

jogar = input('Deseja jogar?\nR: ')


    
while vida_inimigo > 0 and jogar.lower() == 'sim':

    if jogar.lower() != 'sim':
        print('Jogo encerrado!')
        break

    pular_linha()
    print('Seu turno!')
    pular_linha()
    

    jogador_danos = [1,2,3]

    Movimentos = input('[1]soco\n[2]chute\n[3]Correr\nR: ')

    if Movimentos == '1':
        print('Você deu um soco!')
        dano = random.choice(jogador_danos)
        print(f'Voce Deu {dano} de dano')
        print(f'A vida do inimigo é de {vida_inimigo-dano}/10')
        vida_inimigo = vida_inimigo - dano


        pular_linha()

        if vida_inimigo <= 0:
            print('Você venceu!')

    elif Movimentos == '2':
        print('Você deu um chute!')
        dano = random.choice(jogador_danos)
        print(f'Voce Deu {dano} de dano')
        print(f'A vida do inimigo é de {vida_inimigo-dano}/10')
        vida_inimigo = vida_inimigo - dano

        pular_linha()

        if vida_inimigo <= 0:
            print('Você venceu!')

    elif Movimentos == '3':
        print('Você conseguiu fugir!!!')

        jogar = input('Quer jogar denovo?\nR: ')
        if jogar.lower() != 'sim':
            print('Obrigado por jogar')
            break
    
  
else:
    print('Erro!!')