def pagamento():
    from os import system
    print('-----')
    print('Bem vindo ao Pagamento')
    print('-----')
    
    cont=0
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
                    cont=cont+1
                    conta=float(input('Digite o valor da conta do cliente {} ou zero para encerrar: '.format(cliente)))
                except ValueError:
                    print('Valor da conta invalido')
                    cont=0
                except:
                    print('Erro conta')
                    cont=0
                else:
                    if conta==0:
                        cont=0
                        break
                    list_conta.append(conta)    
                    try:
                        atraso=int(input('Digite quantos dias a conta do cliente {} está atrasada '.format(cliente)))
                    except ValueError:
                        print('Dias de atraso invalido')
                    except:
                        print('Erro atrasdo')
                    else:
                        list_atraso.append(atraso)
                        if atraso>0:
                            try:
                                multa=float(input('Valor da multa = '))
                                juros=float(input('Valor dos juros = '))
                            except ValueError:
                                print('Multa e juros invalidos')
                            except:
                                print('Erro multa juros')
                            else:
                                valor=conta+(conta*(multa/100)+conta*(atraso*(juros/100)))
                                list_valor.append(valor)
                        if atraso==0:
                            list_valor.append(conta)
                            valor_final=sum(list_valor)
                            list_valor_final.append(valor_final)
                                    
            try:
                print('-----')
                print('Valor total das contas = ',valor_final)
                print('-----')
                dinheiro=float(input('Valor repassado do cliente $: '))
                troco=dinheiro-valor_final
                print('-----')
                print('troco = ',troco)
                print('-----')
            except ValueError:
                print('valor repassado invalido')
            except:
                print('Erro repasse')    
            else:            
                if dinheiro<valor_final:
                    print('Repasse a menor')
                while dinheiro>valor_final:
                    retorno=float(input('Troco para o cliente: '))
                    troco=troco-retorno
                    print('Troco= ',troco)
                    if troco==0:
                        break
                list_conta.clear()
                list_valor.clear()
        system('pause')
        system('cls')                                
                    
                    
                    
pagamento()    
    