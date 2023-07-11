def pagamento():
    print('-Bem vindo ao pagamento de boletos-')
    cont=0
    list_cliente=[]
    list_conta=[]
    list_atraso=[]
    list_pagar=[]
    try:
        while True:
            cliente=(input('Digite o nome do cliente ou zero para encerrar = '))
            list_cliente.append(cliente)
            if cliente=='0':
                list_cliente.pop(-1)
                break
            try:
                cont=0
                while True:
                    cont=cont+1
                    conta=float(input('Valor da {}ª conta do cliente {} ou zero para encerrar = '.format(cont,cliente)))
                    list_conta.append(conta)
                    if conta==0:
                        list_conta.pop(-1)
                        break
                    try:
                        atraso=int(input('A {}ª conta do cliente {} está atrasada?. Quantos dias?. (Sem atraso digite zero) =  '.format(cont,cliente)))
                        list_atraso.append(atraso)
                        if atraso>0:
                            try:
                                multa=float(input('Valor da multa = '))
                                juros=float(input('Valor dos juros = '))
                                pagar=conta+(conta*(multa/100))+(conta*(juros/100)*atraso)
                                list_pagar.append(pagar)
                            except ValueError:
                                print('Multa ou juros invalido')
                            except:
                                print('Erro')
                        elif atraso==0:
                            list_pagar.append(conta)
                        valor=list_pagar(sum)
                        print(valor)
                        try:
                            dinheiro=float('Valor entregue pelo cliente = ')
                        except ValueError:
                            print('Valor entregue pelo clinte inválido')
                        except:
                            print('Erro')
                        else:
                            troco=dinheiro-valor
                            while troco==0:
                                print(troco)
                                dinheiro=float('Valor entregue pelo cliente ou zero para encerrar = ')
                    except ValueError:
                        print('Atraso em dias invalido')
                    except:
                        print('Erro')
            except ValueError:
                print('Conta digitada invalida!!. Digite novamente!!')
            except:
                print('Erro')
    except ValueError:
        print('Nome do cliente inválido!!. Digite novamente!!')
    except:
        print('Erro')
    print(list_cliente)
    print(list_conta)
pagamento()
print(list)