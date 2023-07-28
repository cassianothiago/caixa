class Pagamento():
    def __init__(self,conta,atraso):
        self.conta=conta
        self.atraso=atraso
        

class Conta_Atraso(Pagamento):
    def __init__(self, conta, atraso):
        super().__init__(conta, atraso)
    
    def com_atraso(self,conta,multa,juros,atraso):
        atraso=self.atraso
        conta=self.conta*(multa/100)+(self.conta*juros/100)*atraso
        return conta
        
class Conta_em_dia(Pagamento):
    def __init__(self,conta, atraso):
        super().__init__(conta, atraso)
        
        
    def sem_atraso(self,conta): 
        conta=self.conta  
        return conta
            
'''class Troco():
    def dev_troco(self,valor,dinheiro):
        troco=dinheiro-valor
        print(troco)
        while troco!=0:
            dinheiro=float(input('Valor a receber: '))
            troco=troco-dinheiro
            print(troco)
            if troco==0:
                print(troco)
                break
        if troco==0:
            print(troco)'''
                
            
    
        
            
    