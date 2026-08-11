def filtrar(leads: list[dict]):
    qualificados = []
    for lead in leads:
        if lead.get('score') >= 70:
            qualificados.append(lead)
            print(lead.get('nome'))

def taxa_conversao(leads: list[dict]):
    totais : dict[str, int] = {}
    ganho : dict[str, int] = {}
    
    for lead in leads:
        origem = lead.get('origem')
        status = lead.get('status')
        
        if origem not in totais:
            totais[origem] = 0
            ganho[origem] = 0
        
        totais[origem] += 1
        if status == 'ganho':
            ganho[origem] += 1
            
    # cálculo da taxa de conversão
    for origem in totais:   
        t = totais.get(origem)
        g = ganho.get(origem)
        taxa = g / t if t > 0 else 0
        print(f'{origem} --> {(taxa*100):.2f}%')
            
# função main
def main():
    leads = [
        {"nome":"Ana","origem":"Instagram","score":82,"status":"ganho"},
        {"nome":"Beta","origem":"Google Ads","score":65,"status":"perdido"},
        {"nome":"Cris","origem":"Indicação","score":90,"status":"ganho"},
        {"nome":"Duda","origem":"Instagram","score":74,"status":"perdido"},
        {"nome":"Enzo","origem":"Google Ads","score":71,"status":"ganho"},
    ]
    
    # filtrando os leads com score maior ou igual a 70
    filtrar(leads)
    
    # taxa de conversão por origem
    taxa_conversao(leads)

            
# programa principal
if __name__ == '__main__':
    main()