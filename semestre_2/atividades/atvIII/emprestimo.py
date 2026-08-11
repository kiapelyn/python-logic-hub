

class Emprestimo:
    
    def __init__(self, vlr_financiado: float, tx_juros_mensal: float, nm_parcelas: int, id_emprestimo:str, nome_cliente:str):
        self.P = vlr_financiado
        self.i = tx_juros_mensal / 100
        self.n = nm_parcelas
        self.id_emprestimo = id_emprestimo
        self.nome_cliente = nome_cliente
        
    #a) Método para calcular e retornar o valor da parcela (fixa) pelo método PRICE. O cálculo da parcela é realizado utilizando a seguinte expressão:
    def calcular_parcela(self) -> float:
        if self.i < 0:
            return 0.0
        elif self.i == 0:
            vlr_parcela = self.P / self.n
        else:
            d = 1 - (1 + self.i) ** (-self.n)
            vlr_parcela = self.P * (self. i / d)
            
        return vlr_parcela
    
    # b) método para retornar o saldo devedor após o pagamento da k-ésima parcela (k ≥ 0). Fórmula fechada para PRICE (se 𝑖 > 0):
    def saldo_devedor(self, k: int) -> float:
        if k >= self.n:
            return 0.0
        
        if self.i == 0:
            # E se i=0? não diz... saldo linear?
            
            '''se i==0 ent n tem juros amg, é só, é só o valor do emprestimo/numero de parcelas,
            cada vez q vc paga uma parcela vc diminui o exato valor do calcular_parcela
            vc começa devendo p e diminui k vezes o valor da parcela'''
            
            return self.P - (k * self.calcular_parcela())
        
        else: 
            res1 = self.P * ((1 + self.i) ** k)
            res2 = self.calcular_parcela() * (((1 + self.i) ** k) - 1) / self.i
            res = res1 - res2
        return res
    
    # c) método para calcular e retornar o valor total de juros pagos ao final do financiamento. A expressão é dada por:J = n * parcela - vlrFinanciado
    def calcular_vlr_total_juros(self) -> float:
        J = self.n * self.calcular_parcela() - self.P
        return J
    
    
    def __str__(self) -> str:
        custo_total = self.calcular_parcela() * self.n
        return f'Plano {self.id_emprestimo} – {self.n:<3}x | Parcela: R$ {self.calcular_parcela():<10.2f} | Juros Totais: R$ {self.calcular_vlr_total_juros():<10.2f} | Custo Total: R$ {custo_total:.2f}'
    
    
        