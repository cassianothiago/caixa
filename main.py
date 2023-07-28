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
        else:
            if conta>0:
                atraso=input('A conta do cliente {} está atrasada? sim ou não:. '.format(nome))
                if atraso=='não' or 'NÃo':
                    dias=0
                    pagar=Pagamento(nome,conta,dias)
                    em_dia=Conta_em_dia
                    em_dia.sem_atraso(conta)
                    list_conta.append(conta)
                elif atraso=='sim' or 'Sim' or 'SIM' or 'sIm' or 'siM' or 'SIm' or 'SiM':
                    try:
                        dias=int(input('Quantos dias? = '))
                    except ValueError:
                        print('Dias inválidos')
                    except:
                        print('Erro dias')
                    else:
                        list_dias.append(dias)
                        pagar=Pagamento(nome,conta,dias)
                        try:
                            multa=float(input('Valor da multa = '))
                            juros=float(input('Valor do juros = '))
                        except ValueError:
                            print('Multa e Juros inválidos!!')
                        except:
                            print('Erro Multa e Juros')
                        else:  
                            atrasado=Conta_Atraso
                            atrasado.com_atraso(multa,juros)
                            list_conta.append(conta)
    
    print(sum(list_conta))
    print(list_nome)
    print(list_dias)                        
                        
                    
            


