class Pagamento():
    def __init__(self,nome,conta,atraso):
        self.nome=nome
        self.conta=conta
        self.atraso=atraso
        

class Conta_Atraso(Pagamento):
    def __init__(self, nome, conta, atraso):
        super().__init__(nome, conta, atraso)
    
    def atraso(self,multa,juros):
        if self.atraso>0:
            self.conta=self.conta*(multa/100)+self.conta*(self.atraso*(juros/100))
            return self.conta
        elif self.atraso==0:
            return self.conta
        else:
            print('valor da conta inválido')
            
class Troco():
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
            print(troco)
                
            
    
        
            
    