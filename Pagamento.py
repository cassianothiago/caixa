def pagamento():
    from os
    print('-----')
    print('Bem vindo ao Pagamento')
    print('-----')
    
    cont=0
    list_cliente=[]
    list_conta=[]
    list_atraso=[]
    list_valor=[]
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
                    conta=float(input('Digite o valor da {}ª conta do cliente {} ou zero para encerrar: '.format(cont,cliente)))
                except ValueError:
                    print('Valor da conta invalido')
                except:
                    print('Erro conta')
                else:
                    if conta==0:
                        cont=0
                        break
                    list_conta.append(conta)    
                    try:
                        atraso=int(input('Digite quantos dias a {}ª conta do cliente {} está atrasada '.format(cont,cliente)))
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
                                        
            
                    
                    
pagamento()    
    