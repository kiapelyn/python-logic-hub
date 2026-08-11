"""
    a) Filtrar apenas os leads qualificados (score ≥ 70).
    b) Calcular a taxa de conversão por origem:
    taxa origem = nº de ganhos na origem/nº total de leads na origem 
    considerando convertido quando status == ganho
"""

leads = [
{"nome":"Ana","origem":"Instagram","score":82,"status":"ganho"},
{"nome":"Beto","origem":"Google Ads","score":65,"status":"perdido"},
{"nome":"Cris","origem":"Indicação","score":90,"status":"ganho"},
{"nome":"Duda","origem":"Instagram","score":74,"status":"perdido"},
{"nome":"Enzo","origem":"Google Ads","score":71,"status":"ganho"},
]

taxa = {}
original = {}

for i in range(len(leads)):
    pessoa = leads[i]
    if pessoa.get('score') >= 70:
        print(f"{leads[i]['nome']}: {leads[i]['score']}")
        
print()
for i in range(len(leads)):
    origem = leads[i]['origem']
    status = leads[i]['status']
    if status == 'ganho':
        if leads[i]['origem'] in taxa:
            taxa[origem] += 1
        else:
            taxa[origem] = 1
              
for i in range(len(leads)):
    origem = leads[i]['origem']
    status = leads[i]['status']
    if leads[i]['origem'] in original:
        original[origem] += 1
    else:
        original[origem] = 1
  
for origem in original:
    tx = taxa.get(origem)
    og = original.get(origem)
    ganho = (tx / og) * 100 if og > 0 else 0
    print(f"{origem}: {ganho:.2f}%")