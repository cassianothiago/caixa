'''from os import system
cont=0
list_cliente=[]
while True:
            try:
                print('--Bem vindo ao pagamento--')
                print('-----')
                cont=cont+1
                cliente=input('Digite o nome do {}º cliente ou zero para encerrar: '.format(cont))
                system('pause')
                system('cls')
                if cliente=='0':
                    list_cliente.append(cliente)
                    list_cliente.pop(-1)
                    break
                print(list_cliente)
            except ValueError:
                print('Nome digitado invalido!! Digite novamente')
            except:
                print('erro!! Digite novamente')'''
from Pagamento import*
print('-----')
cont=0
while True:
    
    
   