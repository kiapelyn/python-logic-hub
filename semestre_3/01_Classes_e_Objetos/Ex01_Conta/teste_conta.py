from conta import Conta

conta = Conta("Semininim")

valor_depo = 1000
valor_tirar = 500
valor_transferir = 200
conta_fantasma = Conta("Fafinha")

if conta.depositar(valor_depo) == False:
    print("O valor depositado deve ser maior que R$0,00")
else: print(f"Valor depositado com sucesso. Saldo atual: R${conta.saldo:.2f}")
print()
if conta.sacar(valor_tirar) == False:
    print(f"Saldo insuficiente. Saldo atual: R${conta.saldo:.2f}")
else: print(F"Saque realizado com sucesso. Saldo atual: R${conta.saldo:.2f}")
print()
if conta.transferir(valor_transferir, conta_fantasma) == False:
    print(f"Saldo insuficiente. Saldo atual: R${conta.saldo:.2f}")
else: 
    print(F"Transferência de {conta.titular} no valor de R${valor_transferir:.2f} para {conta_fantasma.titular} realizada com sucesso.")
    print(f"Saldo atual de {conta.titular}: R${conta.saldo:.2f}")
    print(f"Saldo atual de {conta_fantasma.titular}: R${conta_fantasma.saldo:.2f}")
print()
print(conta)