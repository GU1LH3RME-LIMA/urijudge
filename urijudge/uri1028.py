def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

# Exemplo de uso



if __name__ == "__main__":
    N=int(input())
    for i in range(N):
        i,j=map(int,input().split())
        print(mdc(i, j))
