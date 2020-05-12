print ("Ingresa el tamaño de las matrices ")
numero = int(input())

matriz = []
matrizResultado = []

for i in range(numero):
    matriz.append([0]* numero)

for f in range(numero):
    for c in range(numero):
        matriz[f][c] = int (input("Elemento de la matriz uno  %d, %d :" % (f,c)))

print("Matriz 1")
for i in range(numero):
    acomoda = []
    for j in range(numero):
        acomoda.append(matriz[i][j])
    print(acomoda)

matriz2 = []

for i in range(numero):
    matriz2.append([0]* numero)

for f in range(numero):
    for c in range(numero):
        matriz2[f][c] = int (input("Elemento de la matriz 2 %d, %d :" % (f,c)))

print("Matriz 2")
for i in range(numero):
    acomoda = []
    for j in range(numero):
        acomoda.append(matriz2[i][j])
    print(acomoda)


op = 0
while op==0:
    print ("Que decea hacer con las matrizes ")
    print ("Marque 1 para sumar")
    print ("Marque 2 para restar ")
    print ("Marque 3 para multiplicar")
    print ("Marque 4 para salir")
    opcion = int(input())

    if (opcion==1):
        for a in range(numero):
            matrizResultado.append([0]* numero)
            for b in range(numero):
                matrizResultado[a][b] = ( matriz[a][b] + matriz2[a][b] )
        for i in range(numero):
            acomoda = []
            for j in range(numero):
                acomoda.append(matrizResultado[i][j])
            print(acomoda)   
    elif (opcion==2):
        for a in range(numero):
            matrizResultado.append([0]* numero)
            for b in range(numero):
                matrizResultado[a][b] = ( matriz[a][b] - matriz2[a][b] )
        for i in range(numero):
            acomoda = []
            for j in range(numero):
                acomoda.append(matrizResultado[i][j])
            print(acomoda)
    elif (opcion==3):
        for a in range(numero):
            matrizResultado.append([0]* numero)
            for b in range(numero):
                for d in range(numero):
                    matrizResultado[a][b] += matriz[a][d] * matriz2[d][b]
        for i in range(numero):
            acomoda = []
            for j in range(numero):
                acomoda.append(matrizResultado[i][j])
            print(acomoda)
    elif (opcion==4):
        print ("GOOD BYE")
        op = 4
    else:
        print("No elijio ninguna FIN")



    
    
        



        
        
        

   
