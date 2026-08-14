#lista1 = [1,2,3]
#lista2 = [4,5,6]
#lista3 = [7,8,9]
#matriz = [lista1, lista2, lista3]

#print(matriz[0][0])
#matriz[0][0] = 100

#função criar e retornar matriz
def criar_matriz(n_linhas,n_colunas):
    matriz = [] #lista vazia
    for i in range(n_linhas): #para i no alcance de lista numero de linhas
        linha = []