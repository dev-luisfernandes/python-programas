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
    for linhas in matriz: #percorre cada linha da matriz
        print(linhas) #imprime a linha da matriz

# função para percorrer e imprimir os elementos 1 por 1 da matriz
def imprimir_elementos(matriz):
    for i in range(len(matriz)): #percorre o numero de linhas da matriz
        for j in range(len(matriz[i])): #percorre o numero de colunas da matriz
            print(matriz[i][j]) #imprime o elemento da matriz na posição i,j

#main 
matriz = criar_matriz(3, 3) # chama a função criar_matriz e atribui o resultado à variável matriz
imprimir_matriz(matriz) # chama a função imprimir_matriz passando a matriz como parametro
imprimir_elementos(matriz) # chama a função imprimir_elementos passando a matriz como parametro