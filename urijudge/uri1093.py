
from collections import deque
def probabilidadeVit(EV1, EV2, at, d):
    # Probabilidade de vampiro 1 ganhar um turno
    p1 = at / 6.0
    p2 = (6 - at) / 6.0

    # Dicionário para armazenar probabilidades já calculadas
    prob = {}
    fila = deque()
    fila.append((EV1, EV2))
    prob[(EV1, EV2)] = None  # ainda não calculado

    while fila:
        ev1, ev2 = fila.popleft()

        # Casos base
        if ev1 <= 0:
            prob[(ev1, ev2)] = 0.0
            continue
        if ev2 <= 0:
            prob[(ev1, ev2)] = 1.0
            continue

        # Próximos estados
        prox1 = (ev1 + d, ev2 - d)  # vampiro 1 vence turno
        prox2 = (ev1 - d, ev2 + d)  # vampiro 2 vence turno

        # Se ainda não foram visitados, adiciona na fila
        if prox1 not in prob:
            prob[prox1] = None
            fila.append(prox1)
        if prox2 not in prob:
            prob[prox2] = None
            fila.append(prox2)

        # Se já temos valores resolvidos para os próximos estados
        if prob[prox1] is not None and prob[prox2] is not None:
            prob[(ev1, ev2)] = p1 * prob[prox1] + p2 * prob[prox2]
        else:
            # Recoloca o estado no fim da fila até que os filhos estejam resolvidos
            fila.append((ev1, ev2))

    return prob[(EV1, EV2)]

if __name__ == "__main__":
    while True:
        ev1,ev2,at,d=map(int,input().split())
        condicao = ev1 <= 0 and ev2 > 10 and (at == 0 or at > 5) and (d == 0 or d > 10)
        if condicao:
            break 
        probabilidade=probabilidadeVit(ev1, ev2, at, d)*100
        print(probabilidade)  
