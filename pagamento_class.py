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
            
        
    
        
            
    