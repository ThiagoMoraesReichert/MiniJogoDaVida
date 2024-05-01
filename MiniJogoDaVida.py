# -=-=-=-=-=-=-=-=-=-=-=-= Configurações básicas -=-=-=-=-=-=-=-=-=-=-=-=

import random

numPlayers = int(input('Quantos jogadores?\n1 - Um jogador.\n2 - Dois jogadores.\n'))

jogador1 = 0
jogador1Nome = 'Jogador 1'
filhosJ1 = 0
dinheiroJ1 = 0
numCasamenosJ1 = 0
vidaJ1 = True
casamentoJ1 = False
famaJ1 = False
cursoJ1 = []


jogador2 = 0
jogador2Nome = 'Jogador 2'
filhosJ2 = 0
dinheiroJ2 = 0
numCasamenosJ2 = 0
vidaJ2 = True
casamentoJ2 = False
famaJ2 = False
cursoJ2 = []

# -=-=-=-=-=-=-=-=-=-=-=-= Fim configurações básicas -=-=-=-=-=-=-=-=-=-=-=-=


# -=-=-=-=-=-=-=-=-=-=-=-= Funções -=-=-=-=-=-=-=-=-=-=-=-=

def Dado(nJogador, jogadorNome):
    numSorteado = random.randint(1,6)
    nJogador = ExecutarRegras(nJogador, jogadorNome, numSorteado)
    return nJogador


def ExecutarRegras(nJogador, jogadorNome, dado):
    if dado == 1:
        nJogador += 1
        print(jogadorNome,'tirou',dado)
    if dado == 3:
        nJogador -= 1
        print(jogadorNome,'tirou',dado)

    if dado == 2:
        nJogador += 2
        print(jogadorNome,'tirou',dado)

    if dado == 4:
        nJogador += 4
        print(jogadorNome,'tirou',dado)

    if dado == 5:
        nJogador += 5
        print(jogadorNome,'tirou',dado)

    if dado == 6:
        nJogador += 6
        print(jogadorNome,'tirou',dado)

    elif nJogador < 0:
        nJogador = 0

    elif nJogador > 21:
        nJogador = 21
    return nJogador



def Morrer(nJogador, vidaJogador):
    vidaJogador = False
    print('Game over.', nJogador,'morreu.')
    return vidaJogador

def Formatura(nJogador, curso):
    numSorteado = random.randint(1,6)
    
    if numSorteado == 1:
        cursoJ1.append('Direito')
        print(nJogador,'Acaba de se formar no curso de Direito. Parabéns!')
    elif numSorteado == 2:
        cursoJ1.append('Medicina')
        print(nJogador,'Acaba de se formar no curso de Medicina. Parabéns!')
    elif numSorteado == 3:
        cursoJ1.append('Jogos Digitais')
        print(nJogador,'Acaba de se formar no curso de Jogos Digitais. Parabéns!')
    elif numSorteado == 4:
        cursoJ1.append('Segurança da Informação')
        print(nJogador,'Acaba de se formar no curso de Segurança da Informação. Parabéns!')
    elif numSorteado == 5:
        cursoJ1.append('Análise e Desenvolvimento de Sistemas')
        print(nJogador,'Acaba de se formar no curso de Análise e Desenvolvimento de Sistemas. Parabéns!')
    elif numSorteado == 6:
        cursoJ1.append('Artes Visuais')
        print(nJogador,'Acaba de se formar no curso de Artes Visuais. Parabéns!') 

def TerFilhos(nJogador, filhos):
    numSorteado = random.randint(1,6)
    if numSorteado == 5:
        print(nJogador,'Teve gêmeos!')
        filhos += 2
    else:
        print(nJogador,'Teve um filho!')
        filhos += 1
    return filhos

def Casar(JogadorNome, casar, numCasamentos):
    casar = True
    numCasamentos += 1
    print(JogadorNome,'acabou de se casar!')
    return casar, numCasamentos



def Divorciar(nJogador, casado):
    if casado == True:
        casado = False
        print('O amor acabou...', nJogador,'pediu divórcio.')
    else:
        print(nJogador,'não é casado.')
    return casado


def FicarFamoso(nJogador, fama):
    fama = True
    print(nJogador,'ficou famoso(a)!')

def Loteria(nJogador, dinheiro):
    numSorteado = random.randint(1,6)

    if numSorteado == 1:
        dinheiro += 2.50
    elif numSorteado == 2:
        dinheiro += 5000
    elif numSorteado == 3:
        dinheiro += 50000
    elif numSorteado == 4:
        dinheiro += 500000
    elif numSorteado == 5:
        dinheiro += 5000000
    elif numSorteado == 6:
        dinheiro += 10000000
    
    print(nJogador,'ganhou na loteria!')
    return dinheiro

def Resetar(nJogador, vida, curso, casamento, fama, dinheiro, filhos, numCasamentos):
    nJogador = 0
    vida = True
    curso = []
    casamento = False
    fama = False
    dinheiro = 0
    filhos = 0
    numCasamentos = 0

    return nJogador, vida, curso, casamento, fama, dinheiro, filhos, numCasamentos

def NovoAmor(nJogador, casar, numCasamentos):
    if casar == False and numCasamentos == 0:
        casar = True
        numCasamentos += 1
    (nJogador,'acaba de encontrar uma chance no amor e se casou!')
    return casar, numCasamentos

def DesafioMatematico(nJogador):
    numSorteado = random.randint(1,6)
    print(nJogador,'caiu no desafio matemático:')
    if numSorteado == 1:
        print('\nPrimos até 100:')
        print(primos())
    elif numSorteado == 2:
        print('\nSomatório dos números de 1 até 100:')
        print(somatorio())
    elif numSorteado == 3:
        print('\nFibocci até o décimo elemento:')
        for i in range(10):
            print(fibonacci(i))
    elif numSorteado == 4:
        print('\nÁrea de um círculo com raio 2.5:')
        print(area_circulo(2.5))
    elif numSorteado == 5:
        print('\nFatorial de 5:')
        print(fatorial(5))
    elif numSorteado == 6:
        print('\n5 números divisíveis por 5 e por 2:')
        print(DivisivelPor2e5())


def DivisivelPor2e5():
    cont = 0
    num = 1
    while cont < 5:
        if num % 2 == 0 and num % 5 == 0:
            print(num)
            cont += 1
        num += 1

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def area_circulo(raio):
    return round((3.14 * raio ** 2),2)

def somatorio():
    return sum(range(1, 11))

def primos():
    primos = []
    for possivel_primo in range(2, 101):
        eh_primo = True
        for num in range(2, possivel_primo):
            if possivel_primo % num == 0:
                eh_primo = False
        if eh_primo:
            primos.append(possivel_primo)
    return primos


#-=-=-=-=-=-=-=-=-=-=-=-= Fim Funções -=-=-=-=-=-=-=-=-=-=-=-=

#-=-=-=-=-=-=-=-=-=-=-=-= Modo de jogo - 1 Jogador -=-=-=-=-=-=-=-=-=-=-=-=
if numPlayers == 1:
    while jogador1 != 21:
        jogador1 = Dado(jogador1, jogador1Nome)


        if jogador1 == 0 or jogador1 == 1 or jogador1 == 3 or jogador1 == 10 or jogador1 == 17:
            jogador1 = Dado(jogador1, jogador1Nome)

        elif jogador1 == 2 or jogador1 == 8 or jogador1 == 18:
            vidaJ1 = Morrer(jogador1Nome, vidaJ1)
            if vidaJ1 == False:
                print('\nJogador 1 perdeu.\n')
                break

        elif jogador1 == 4 or jogador1 == 11 or jogador1 == 19:
            pass
        
        elif jogador1 == 5:
            Formatura(jogador1, cursoJ1)
        
        elif jogador1 == 6 or jogador1 == 9 or jogador1 ==13:
            filhosJ1 = TerFilhos(jogador1Nome, filhosJ1)
        
        elif jogador1 == 7:
            casamentoJ1, numCasamenosJ1 = Casar(jogador1Nome, casamentoJ1, numCasamenosJ1)


        elif jogador1 == 12:
            casamentoJ1 = Divorciar(jogador1Nome, casamentoJ1)

        elif jogador1 == 16:
            casamentoJ1, numCasamenosJ1= NovoAmor(jogador1Nome, casamentoJ1, numCasamenosJ1)

        elif jogador1 == 14:
            dinheiroJ1 = Loteria(jogador1Nome, dinheiroJ1)

        elif jogador1 == 15:
            FicarFamoso(jogador1Nome, famaJ1)

        elif jogador1 == 20:
            jogador1, vidaJ1, cursoJ1, casamentoJ1, famaJ1, dinheiroJ1, filhosJ1, numCasamenosJ1 = Resetar(jogador1, vidaJ1, cursoJ1, casamentoJ1, famaJ1, dinheiroJ1, filhosJ1, numCasamenosJ1)

    if jogador1 >= 21:    
        print('\nJogador ganhou! Teve uma vida longa e próspera!\n')
    
    if casamentoJ1 == True:
        casamentoJ1 = 'Casado(a)'
    else:
        casamentoJ1 = 'Solteiro(a)'

    if famaJ1 == True:
        famaJ1 = 'Famoso(a)'
    else:
        famaJ1 = 'Não foi famoso(a)'
    
    if vidaJ1 == False:
        vidaJ1 = 'Jogador está morto(a).'
    else:
        vidaJ1 = 'Jogador está vivo(a)'
    
    if cursoJ1 == []:
        cursoJ1 = 'Nenhum'
    print('---| Status final - Jogador 1: |---\n')
    print('Casa final:',jogador1,'\nFilhos:',filhosJ1,'\nDinheiro:',dinheiroJ1,'\nCurso(s):',cursoJ1,'\nStatus de vida:',vidaJ1,'\nRelacionamento:',casamentoJ1,'\nFama:',famaJ1)

# -=-=-=-=-=-=-=-=-=-=-=-= Fim modo de jogo - 1 Jogador -=-=-=-=-=-=-=-=-=-=-=-=

#-=-=-=-=-=-=-=-=-=-=-=-= Modo de jogo - 2 Jogadores -=-=-=-=-=-=-=-=-=-=-=-=
if numPlayers == 2:
    while jogador1 != 21 or jogador2 != 21:
        jogador1 = Dado(jogador1, jogador1Nome)
        jogador2 = Dado(jogador2, jogador2Nome)

        #-=-=-=-=-=-=-=-=-=-=-=-= Jogador 1 - Mecânicas -=-=-=-=-=-=-=-=-=-=-=-=
        if jogador1 == 0 or jogador1 == 1 or jogador1 == 3 or jogador1 == 10 or jogador1 == 17:
            jogador1 = Dado(jogador1, jogador1Nome)

        elif jogador1 == 2 or jogador1 == 8 or jogador1 == 18:
            vidaJ1 = Morrer(jogador1Nome, vidaJ1)
            if vidaJ1 == False:
                print('\nJogador 1 perdeu.\n')
                break

        elif jogador1 == 4 or jogador1 == 11 or jogador1 == 19:
            DesafioMatematico(jogador1Nome)
        
        elif jogador1 == 5:
            Formatura(jogador1, cursoJ1)
        
        elif jogador1 == 6 or jogador1 == 9 or jogador1 ==13:
            filhosJ1 = TerFilhos(jogador1Nome, filhosJ1)
        
        elif jogador1 == 7:
            casamentoJ1, numCasamenosJ1 = Casar(jogador1Nome, casamentoJ1, numCasamenosJ1)


        elif jogador1 == 12:
            casamentoJ1 = Divorciar(jogador1Nome, casamentoJ1)
        
        elif jogador1 == 16:
            casamentoJ1, numCasamenosJ1= NovoAmor(jogador1Nome, casamentoJ1, numCasamenosJ1)

        elif jogador1 == 14:
            dinheiroJ1 = Loteria(jogador1Nome, dinheiroJ1)

        elif jogador1 == 15:
            FicarFamoso(jogador1Nome, famaJ1)

        elif jogador1 == 20:
            jogador1, vidaJ1, cursoJ1, casamentoJ1, famaJ1, dinheiroJ1, filhosJ1, numCasamenosJ1 = Resetar(jogador1, vidaJ1, cursoJ1, casamentoJ1, famaJ1, dinheiroJ1, filhosJ1, numCasamenosJ1)

        #-=-=-=-=-=-=-=-=-=-=-=-= Fim jogador 1 - Mecânicas -=-=-=-=-=-=-=-=-=-=-=-=

        #-=-=-=-=-=-=-=-=-=-=-=-= Jogador 2 - Mecânicas -=-=-=-=-=-=-=-=-=-=-=-=
        if jogador2 == 0 or jogador2 == 1 or jogador2 == 3 or jogador2 == 10 or jogador2 == 17:
            jogador2 = Dado(jogador2, jogador2Nome)

        elif jogador2 == 2 or jogador2 == 8 or jogador2 == 18:
            vidaJ1 = Morrer(jogador2Nome, vidaJ2)
            if vidaJ2 == False:
                print('\nJogador 2 perdeu.\n')
                break

        elif jogador2 == 4 or jogador2 == 11 or jogador2 == 19:
            DesafioMatematico(jogador2Nome)
        
        elif jogador2 == 5:
            Formatura(jogador2, cursoJ2)
        
        elif jogador2 == 6 or jogador2 == 9 or jogador2 ==13:
            filhosJ2 = TerFilhos(jogador2Nome, filhosJ2)
        
        elif jogador2 == 7:
            casamentoJ2, numCasamenosJ2 = Casar(jogador2Nome, casamentoJ2, numCasamenosJ2)


        elif jogador2 == 12:
            casamentoJ2 = Divorciar(jogador2Nome, casamentoJ2)

        elif jogador2 == 16:
            casamentoJ2, numCasamenosJ2= NovoAmor(jogador2Nome, casamentoJ2, numCasamenosJ2)

        elif jogador2 == 14:
            dinheiroJ2 = Loteria(jogador2Nome, dinheiroJ2)

        elif jogador2 == 15:
            FicarFamoso(jogador2Nome, famaJ2)

        elif jogador2 == 20:
            jogador2, vidaJ2, cursoJ2, casamentoJ2, famaJ2, dinheiroJ2, filhosJ2, numCasamenosJ2 = Resetar(jogador2, vidaJ2, cursoJ2, casamentoJ2, famaJ2, dinheiroJ2, filhosJ2, numCasamenosJ2)

        #-=-=-=-=-=-=-=-=-=-=-=-= Fim jogador 1 - Mecânicas -=-=-=-=-=-=-=-=-=-=-=-=

    if jogador1 >= 21:    
        print('\nJogador 1 ganhou! Teve uma vida longa e próspera!\n')
    elif jogador2 >= 21:
        print('\nJogador 2 ganhou! Teve uma vida longa e próspera!\n')

    elif vidaJ1 == False and vidaJ2 == True:    
        print('\nJogador 2 ganhou! Teve uma vida longa e próspera!\n')
    elif vidaJ2 == False and vidaJ1 == True:
        print('\nJogador 1 ganhou! Teve uma vida longa e próspera!\n')
    
    if casamentoJ1 == True:
        casamentoJ1 = 'Casado(a)'
    else:
        casamentoJ1 = 'Solteiro(a)'

    if casamentoJ2 == True:
        casamentoJ2 = 'Casado(a)'
    else:
        casamentoJ2 = 'Solteiro(a)'

    if famaJ1 == True:
        famaJ1 = 'Famoso(a)'
    else:
        famaJ1 = 'Não foi famoso(a)'
    
    if famaJ2 == True:
        famaJ2 = 'Famoso(a)'
    else:
        famaJ2 = 'Não foi famoso(a)' 
    
    if vidaJ1 == False:
        vidaJ1 = 'Jogador está morto(a).'
    else:
        vidaJ1 = 'Jogador está vivo(a)'

    if vidaJ2 == False:
        vidaJ2 = 'Jogador está morto(a).'
    else:
        vidaJ2 = 'Jogador está vivo(a)'
    
    if cursoJ1 == []:
        cursoJ1 = 'Nenhum'

    if cursoJ2 == []:
        cursoJ2 = 'Nenhum'
    
    print('---| Status final - Jogador 1: |---\n')
    print('Casa final:',jogador1,'\nFilhos:',filhosJ1,'\nDinheiro:',dinheiroJ1,'\nCurso(s):',cursoJ1,'\nStatus de vida:',vidaJ1,'\nRelacionamento:',casamentoJ1,'\nFama:',famaJ1)

    print('\n---| Status final - Jogador 2: |---\n')
    print('Casa final:',jogador2,'\nFilhos:',filhosJ2,'\nDinheiro:',dinheiroJ2,'\nCurso(s):',cursoJ2,'\nStatus de vida:',vidaJ2,'\nRelacionamento:',casamentoJ2,'\nFama:',famaJ2)
