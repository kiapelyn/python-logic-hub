num_conta = int(input("Insira o número da conta: "))

uni = num_conta % 10
dec = (num_conta - uni) //10 % 10
cent = (num_conta) // 100

centena = uni * 100
dezena = dec * 10
unidade = cent

inverso = centena + dezena + unidade

soma = num_conta + inverso

unid = soma % 10
deze = (soma - uni) //10 % 10
cente = (soma) // 100

predigito = cente * 1 + deze * 2 + unid * 3

verif = predigito % 10

print(f"Dígito verficador = {verif}")