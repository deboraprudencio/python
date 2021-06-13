def acha(seq, x):
    ''' (list, float) -> int
        retorna a posicao em que x ocorre na lista, ou None caso contrario
        '''
    for i in range(len(seq)):
        if seq[i] == x: return i
    
    return None

def main():
    ''' programa que le uma sequencia com N elementos e a imprime
        sem repeticoes.
        '''
    n = int(input())
    seq = []

    for i in range(n):
        x = int(input())
        if acha(seq, x) == None: seq.append(x)
    
    print(seq)

main()