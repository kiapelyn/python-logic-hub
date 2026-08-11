# função para cadastrar: recebe N tuplas (nome, idade, cargo) via *args (gather)
def cadastro(*funcionarios):
    lista = []
    for registro in funcionarios:
        nome, idade, cargo = registro
        lista.append({"nome": nome, "idade": int(idade), "cargo": cargo})
    return lista

# atualizar: recebe o dicionário do funcionário + campos a atualizar via **kwargs (scatter)
def atualizar(funcionario, **novos_dados):
    for chave, valor in novos_dados.items():
        funcionario[chave] = valor
    return funcionario


# função principal do programa (sempre chamada a partir do programa principal)
def main():
    # gather: várias tuplas passadas para cadastro(*args)
    funcionarios = cadastro(
        ("Ana", 28, "Analista"),
        ("Bruno", 35, "Gerente"),
        ("Carla", 22, "Estagiária")
    )

    # scatter: dicionário de atualizações espalhado em **kwargs
    dados_ana = {"idade": 29, "cargo": "Analista Pleno"}
    atualizar(funcionarios[0], **dados_ana)

    atualizar(funcionarios[1], cargo="Gerente Sênior")  
    atualizar(funcionarios[2], idade=23)

    # exibir lista final
    print("Funcionários cadastrados/atualizados:")
    for f in funcionarios:
        print(f)

# programa principal
if __name__ == "__main__":
    main()