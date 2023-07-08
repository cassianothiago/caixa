class Pagamento():
    def __init__(self,cliente,conta,atraso,valor):
        self.cliente=cliente
        self.conta=conta
        self.atraso=atraso
        self.valor=valor
        
    def dig_clientes(self):
        from os import system
        self.cliente=cliente
        cont=0
        list_cliente=[]
        while True:
            try:
                print('-----')
                cont=cont+1
                cliente=input('Digite o nome do {}º cliente ou zero para encerrar: '.format(cont))
                if cliente=='0':
                    list_cliente.append(cliente)
                    list_cliente.pop(-1)
                    break
                system('pause')
                system('cls')
            except ValueError:
                print('Nome digitado invalido!! Digite novamente')
            except:
                print('erro!! Digite novamente')
            
    '''def dig_conta(self,conta):
        from os import system
        self.conta=conta
        cont=0
        while True:
            try:
                print('-----')
                cont=cont+1
                conta=float('Digite o valor da {}ª conta do cliente {}'.format(cont,cliente))
                print(conta)'''
            
            
            
                       
                    
                
            
            
            
        
    
    
    
    
