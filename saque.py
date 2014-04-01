'''
Faça um algoritmo para ler um valor a ser sacado em um caixa eletronico, desprezando os centavos.
o caixa possui apenas notas de 50, 20,10,5

sendo

10 notas de 50
10 notas de 20
10 notas de 10
10 notas de 5

Sendo assim, se o usuário quiser sacar 550 reais, o algoritmo podera usar apenas 10 notas de 50 (disponivel no caixa) 2 notas de 20 e 1 de 10.

''*****************************************************************************************************'

Eu fiz o algoritmo, mas não estou conseguindo raciocinar como limitar para que quando sacado um quantia x de dinheiro, não ultrapasse o limite de notas.

Por exemplo: Se coloco o valor de 550 o programa me mostra 11 notas de 50 mas nao pode, tem q me mostrar 10 de 50 2 de 20  e 1 de 10.

Para descobrir a quantidade de notas sacadas usei o operador %. Alguem poderia me dar uma luz ?
'''

nota5 = 5
nota10 = 10
nota20 = 20
nota50 = 50

qtdNota5 = 10
qtdNota10 = 10
qtdNota20 = 10
qtdNota50 = 10

valMaxSacar = qtdNota5*(nota5 + nota10 + nota20 + nota50)

qt5usada = 0
qt10usada = 0
qt20usada = 0
qt50usada = 0

while(True):
    sac = int(input('Digite o valor que deseja sacar: ')) #não estou fazendo tratamento de erros

    if(sac <= valMaxSacar):

        if(sac%5 == 0):
            
            if(sac//nota50 <=qtdNota50):
                qt50usada = sac//nota50
                
            else:
                qt50usada = qtdNota50

            sac = sac - nota50*qt50usada
            

            if(sac != 0):
                
                if(sac//nota20 <=qtdNota20):
                    qt20usada = sac//nota20
                else:
                    qt20usada = qtdNota20

                sac = sac - nota20*qt20usada
                

            if(sac != 0):
                if(sac//nota10 <=qtdNota10):
                    qt10usada = sac//nota10
                else:
                    qt10usada = qtdNota10

                sac = sac - nota10*qt10usada
                

            if(sac != 0):
                if(sac//nota5 <=qtdNota5):
                    qt5usada = sac//nota5
                else:
                    qt5usada = qtdNota5

                sac = sac - nota5*qt5usada

            break

        else:
            print('Valor não é multiplo de 5')

    else:
        print('Valor ultrapassou o limite de caixa')
                
print('Foram usadas: ',qt50usada,'notas de 50')
print(qt20usada,'notas de 20')
print(qt10usada,'notas de 10')
print(qt5usada,'notas de 5')
