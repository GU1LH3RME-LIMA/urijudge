def diamantes(entrada):
    pilha = []
    diamantes = 0
    for c in entrada:
        if c == '<':
            pilha.append(c)
        elif c == '>' and pilha:
            pilha.pop()
            diamantes += 1
    return diamantes

if __name__ == '__main__':
    n=int(input())  
    for i in range(0,n):
        L=(input())       
        S=diamantes(L)
        print(S)