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
        linha = [] #lista vazia
        for j in range(n_colunas): #for j no alcance de lista numero de colunas
            n = int(input('numero:')) # n recebe o numero digitado pelo usuario
            linha.append(n) #adiciona o numero digitado na lista linha
        matriz.append(linha) #adiciona a lista linha na lista matriz
    return matriz # retorna a matriz

#funnção imprimir e percorrer os elementos da matriz
def imprimir_matriz(matriz): # recebe a matriz como parametro
    print('Matriz:') #imprime a palavra matriz
    for linha in matriz:
#main 
matriz = criar_matriz(3, 3)
imprimir_matriz(matriz) #chama a função imprimir_matriz passando a matriz como parametro