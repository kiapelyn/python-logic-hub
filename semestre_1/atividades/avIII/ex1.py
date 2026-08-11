def coletar_dados():
    qnt = int(input("Quantos pacientes serão monitorados? "))
    for i in range(qnt):
        nome.append(input("Nome do paciente: "))
        temp.append(float(input("Temperatura do paciente: ")))
        pressao.append(int(input("Pressão arterial sistólica do paciente: ")))
    return nome, temp, pressao
            
def verificar_febre():
    for i in range(len(temp)):
        if temp[i] > 37.8:
            print(f"Paciente {nome[i]} está com febre ({temp[i]:.1f}ºC)")
  
def imprimir_status():        
    for i in range(len(nome)):
        if temp[i] <= 37.5 and pressao[i] <= 130:
            print(f"Paciente {nome[i]} está em risco baixo")
        elif (temp[i] < 37.5 and temp[i] > 38.6) or (pressao[i] > 130 and pressao[i] < 151):
            print(f"Paciente {nome[i]} está em risco moderado")
        elif temp[i] > 38.5 or pressao[i] > 150:
            print(f"Paciente {nome[i]} está em risco alto")
        else:
            print(f"Paciente {nome[i]} não tem status de classificação")


nome = []
temp = []
pressao = []

coletar_dados()
verificar_febre()
imprimir_status()