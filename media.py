print('=== MEDIA ANUAL ===')
print('QUANTO CADA SEMESTRE VALE?')
print('__PRIMEIRO SEM 40%__')
print('__SEGUNDO SEM 60%__')

def NotasCp1():
    cp1 = float(input('qual nota da primeira cp?'))
    cp2 = float(input('qual nota da segunda  cp?'))
    cp3 = float(input('qual nota da terceira cp?'))
    Cps1 = [cp1, cp2, cp3]
    Cps1.sort()
    Cps1.pop(0)
    print(Cps1)
    soma_item = 0
    for item in Cps1:
        soma_item = soma_item + item
    return soma_item
    
soma_item_retornada = NotasCp1()
print(soma_item_retornada)
    

