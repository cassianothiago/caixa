def pagamento():
    from os import system
    print('-----')
    print('Bem vindo ao Pagamento')
    print('-----')
    

    multa=False
    juros=False
    atraso1=False
    list_cliente=[]
    list_conta=[]
    list_atraso=[]
    list_valor=[]
    list_valor_final=[]
    while True:
        try:
            cliente=input('Digite o nome do cliente ou zero para encerrar: ')
        except ValueError:
            print('Nome do cliente invalido')
        except:
            print('Erro cliente')
        else:
            if cliente=='0':   
                break
            list_cliente.append(cliente)
            while True:
                try:    
                    conta=float(input('Digite o valor da conta do cliente {} ou zero para encerrar: '.format(cliente)))
                    atraso1=False
                except ValueError:
                    print('Valor da conta invalido')
                except:
                    print('Erro conta')
                else:  
                    list_conta.append(conta)
                    if conta!=0:
                        while atraso1==False:
                            try:
                                atraso1=True
                                atraso=int(input('Digite quantos dias a conta do cliente {} está atrasada '.format(cliente)))
                            except ValueError:
                                print('Dias de atraso invalido')
                                atraso1=False
                            except:
                                print('Erro atrasado')
                                atraso1=False
                                if atraso>0 and atraso1==True:
                                    list_atraso.append(atraso)
                                    atraso1=True
                                    while multa==False and juros==False:
                                        try:
                                            atraso1=True
                                            multa=float(input('Valor da multa = '))
                                            juros=float(input('Valor dos juros = '))
                                            multa=True
                                            juros=True
                                        except ValueError:
                                            print('Multa e juros invalidos')
                                            multa=False
                                            juros=False
                                        except:
                                            print('Erro multa juros')
                                            multa=False
                                            juros=False
                                        else:
                                            atraso1=True
                                            valor=conta+(conta*(multa/100)+conta*(atraso*(juros/100)))
                                            list_valor.append(valor)
                                            multa=True
                                            juros=True
                                elif atraso==0:
                                    list_atraso.append(atraso)
                                    atraso1=True
                                    multa=True
                                    juros=True
                                    list_valor.append(conta)                                                                
                    if conta==0:
                        break          
            try:
                valor_final=sum(list_valor)
                list_valor_final.append(valor_final)
                print('-----')
                print('Valor total das contas = {:.2f}'.format(valor_final))  
                print('-----')
                dinheiro=float(input('Valor repassado do cliente $: '))
                troco=dinheiro-valor_final
                print('-----')
                print('troco = {:.2f}'.format(troco))
                print('-----')
            except ValueError:
                print('valor repassado invalido')
            except:
                print('Erro repasse')    
            else:          
                while dinheiro<valor_final:
                    print('Repasse a menor')
                    print('Devolva o dinheiro e repita o repasse do cliente')
                    print('-----')
                    dinheiro=float(input('Valor repassado do cliente $: '))
                    troco=dinheiro-valor_final
                    print('-----')
                    print('troco = {:.2f}'.format(troco))
                    print('-----')
                while dinheiro>valor_final:
                    retorno=float(input('Troco para o cliente: '))
                    troco=troco-retorno
                    print('Troco= {:.2f}'.format(troco))
                    if troco==0:
                        break
                list_conta.clear()
                list_valor.clear()
        system('pause')
        system('cls')                
    while True:            
                imprimir=(input('Digite I para imprimir a fita de caixa ou o nome do cliente para imprimir específico e zero para fechar pagamento:  ')) 
                if imprimir=='0':
                    break
                if imprimir =='I' or imprimir=='i':
                    print(list_cliente)
                    print(list_atraso)
                    print(list_valor_final)
                else:
                    elemento=len(list_cliente)
                    print(list_cliente[len(elemento)])
                    print(list_atraso[i])
                    print(list_valor_final[i])
    while True:                  
        imprimir=(input('Digite I para imprimir a fita de caixa ou o nome do cliente para imprimir específico e zero para fechar pagamento:  ')) 
        if imprimir=='0':
            break
        if imprimir =='I' or imprimir=='i':
            print(list_cliente)
            print(list_atraso)
            print(list_valor_final)
        else:
            try:
                a=list_cliente.index(imprimir)
                print(a)
                print(list_cliente[a])
                print(list_atraso[a])
                print(list_valor_final[a])
            except ValueError:
                print('cliente não encontrado')
            except:
                print('cliente inválido!')
                        

                
              
                                            

pagamento()    
    