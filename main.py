from pagamento_class import*
from os import system
print('-----')
print('-Bem vindo ao pagamento-')
print('----- \n')

list_nome=[]
list_conta=[]
list_dias=[]

while True:
    nome=input('Digite o nome do cliente ou zero(0) para encerrar o atendimento:. ')
    list_nome.append(nome)
    if nome=='0':
        break
    while True:
        try:
            conta=float(input('Digite o valor da conta do cliente {} ou zero(0) quando não hover mais conta = '.format(nome)))
            if conta==0:
                break
        except ValueError:
            print('Valor da conta inválido!')
        except:
            print('Error conta')
            if conta>0:
                list_conta.append(conta)
                atraso=input('A conta do cliente {} está atrasada? sim ou não:. '.format(nome))
                if atraso=='não' or 'NÃo':
                    
                if atraso=='sim' or 'Sim' or 'SIM' or 'sIm' or 'siM' or 'SIm' or 'SiM':
                    try:
                        dias=int('Quantos dias? = ')
                    except ValueError:
                        print('Dias inválidos')
                    except:
                        print('Erro dias')
                    else:
                        list_dias.append(dias)
                        pagar=Conta_Atraso(nome,conta,dias)
                        pagar.atraso()
                        
                    
            


