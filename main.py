from pagamento_class import*
from os import system
print('-----')
print('-Bem vindo ao pagamento-')
print('----- \n')

list_nome=[]
list_contas=[]
list_dias=[]

while True:
    nome=input('Digite o nome do cliente ou zero(0) para encerrar o atendimento:. ')
    list_nome.append(nome)
    if nome=='0':
        break
    while True:
        try:
            contas=float(input('Digite o valor da conta do cliente {} ou zero(0) quando não hover mais conta = '.format(nome)))
            if contas==0:
                break
        except ValueError:
            print('Valor da conta inválido!')
        except:
            print('Error conta')
        else:
            if contas>0:
                atrasado=input('A conta do cliente {} está atrasada? "s" para sim e "n" para não:. '.format(nome))
                if atrasado=='n' or atrasado=='N':
                    em_dia=Conta_em_dia
                    list_contas.append(contas)
                elif atrasado=='s' or atrasado=='S':
                    try:
                        dias=int(input('Quantos dias? = '))
                    except ValueError:
                        print('Dias inválidos')
                    except:
                        print('Erro dias')
                    else:
                        list_dias.append(dias)
                        try:
                            multa=float(input('Valor da multa = '))
                            juros=float(input('Valor do juros = '))
                        except ValueError:
                            print('Multa e Juros inválidos!!')
                        except:
                            print('Erro Multa e Juros')
                        else:  
                            atrasado=Conta_Atraso(contas,dias)
                            atrasado.com_atraso(contas,dias,multa,juros)
                            list_contas.append(contas)
    
    print(sum(list_contas))
    print(list_nome)
    print(list_dias)                        
                        
                    
            


