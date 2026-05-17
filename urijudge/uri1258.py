def processar_casos():
    primeiro = True
    while True:
        N = int(input().strip())
        if N == 0:
            break

        camisetas = []
        for _ in range(N):
            nome = input().strip()
            cor_tam = input().strip().split()
            cor, tamanho = cor_tam[0], cor_tam[1]
            camisetas.append((cor, tamanho, nome))

        # Ordenação: cor asc, tamanho desc, nome asc
        camisetas.sort(key=lambda x: (x[0], 
                                      {'G':3, 'M':2, 'P':1}[x[1]], 
                                      x[2]))
        
        if not primeiro:
            print()
        primeiro = False
        for cor, tamanho, nome in camisetas:
            print(f"{cor} {tamanho} {nome}")
        
if __name__ == "__main__":
    processar_casos()
