# este exercício eu acabei deixando ele bem mais completo do que faríamos na sala. Portanto, não
# é a única solução, como todos os códigos que fazemos.

# calcula métricas por canal: média, contagem, muito bons (>=9) e críticos (<=4)
def calcular_metricas(respostas):
    soma = {}        # soma das notas por canal
    cont = {}        # contagem por canal
    bons = {}        # >= 9 por canal
    criticos = {}    # <= 4 por canal

    for r in respostas:
        canal = r["canal"]
        nota = float(r["nota"])

        if canal not in soma:
            soma[canal] = 0.0
            cont[canal] = 0
            bons[canal] = 0
            criticos[canal] = 0

        soma[canal] += nota
        cont[canal] += 1

        if nota >= 9:
            bons[canal] += 1
        if nota <= 4:
            criticos[canal] += 1

    metricas = {}
    for canal in cont:
        media = soma[canal] / cont[canal]
        metricas[canal] = {
            "media": round(media, 2),
            "contagem": cont[canal],
            "muito_bons": bons[canal],
            "criticos": criticos[canal],
        }
    return metricas


# filtra respostas por limiar e operador (">=", "<=", ">", "<")
def filtrar_por_limiar(respostas, limiar=9, operador=">="):
    filtradas = []
    for r in respostas:
        nota = float(r["nota"])
        if operador == ">=" and nota >= limiar:
            filtradas.append(r)
        elif operador == "<=" and nota <= limiar:
            filtradas.append(r)
        elif operador == ">" and nota > limiar:
            filtradas.append(r)
        elif operador == "<" and nota < limiar:
            filtradas.append(r)
    return filtradas


# função principal do programa
def main():
    respostas = [
        {"canal": "app",       "nota": 9.5},
        {"canal": "app",       "nota": 8.0},
        {"canal": "site",      "nota": 7.0},
        {"canal": "site",      "nota": 9.0},
        {"canal": "telefone",  "nota": 4.0},
        {"canal": "telefone",  "nota": 3.5},
        {"canal": "loja",      "nota": 10},
        {"canal": "loja",      "nota": 6.0},
    ]

    metricas = calcular_metricas(respostas)
    print("=== Métricas por canal ===")
    for canal in metricas:
        m = metricas[canal]
        print(f"{canal}: média={m['media']}, contagem={m['contagem']}, "
              f"muito_bons={m['muito_bons']}, críticos={m['criticos']}")

    print("\n=== Muito bons (>= 9) ===")
    for r in filtrar_por_limiar(respostas, 9, ">="):
        print(f"{r['canal']} - nota {r['nota']}")

    print("\n=== Críticos (<= 4) ===")
    for r in filtrar_por_limiar(respostas, 4, "<="):
        print(f"{r['canal']} - nota {r['nota']}")

# programa principal
if __name__ == "__main__":
    main()