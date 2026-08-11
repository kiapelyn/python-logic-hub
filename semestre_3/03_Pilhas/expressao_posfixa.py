from collections import deque

# usando A + b * c + d ^ f
def prioridade(operador: str) -> int:
    match operador:
        case '(': return 1
        case '+' | '-': return 2
        case '/' | '*' | '%': return 3
        case '^': return 4
        case _: return 0
        
def converter(expressao: str) -> str:
    pilha = deque()
    posfixa = ''
    
    for ch in expressao:
        if ch != ' ':
            if ch in ('+','-','*','/','%','^'):
                while pilha and (prioridade(pilha[-1]) >= prioridade(ch)): 
                    posfixa += pilha.pop() #remove o último elemento
                pilha.append(ch) # entra direto o +, depois o * pois tem mais prioridade ent n sai (expressão: AB)
                                 # na terceira com o +, sai o * e p + pela prioridade do que está dentro ser maior ou igual (expressão: ABC *+)
                                 # depois, com a pilha vazia, entra o + e depois o ^ pela prioridade (expressão: ABC*+DF)
                                 # ficou coisa na pilha ainda que precisa ser tirado
            elif ch == '(':
                pilha.append(ch)
            elif ch == ')':
                while pilha[-1] != '(':
                    posfixa += pilha.pop()
                pilha.pop()
            else:
                posfixa += ch
                
    # esvazia toda a pilha caso tenha sobrado algum objeto
    while pilha:
        posfixa += pilha.pop() # joga o ^ e o + na expressão --> ABC*+DF^+
        
    return posfixa

#terminar depois
def calcular(posfixa):

    for ch in posfixa:
        pilha = deque()
        if ch not in ('+','-','*','/','%','^'):
            pilha.append(float(ch))
        else: 
            op1, op2 = pilha.pop(), pilha.pop()
            
    return calculo
                            
#principal
expressao = input('Informe a expressão infixa --> ')
posfixa = converter(expressao)
calculo = calcular(posfixa)
print(posfixa)
print(calculo)