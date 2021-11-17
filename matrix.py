import numpy
from numpy import linalg
import matplotlib.pyplot as plt
import math

total = input('Número de pisos: ')
total = int(total)

n = 1
eigenvalores = 0
todos_eigenvalores = []

while n <= total:


    mass_value = 1000
    k_value = 10000

    #Creamos línea de cada matriz#



    c = 0
    piso = ''

    while c<= n-1:
        if c == n-1:
            piso = piso + '0'
            break
        piso = piso  + '0 '

        c = c + 1
    piso = piso + ';'
    #print(piso)


    counter = 0
    matriz = ''
    current = ''
    k = 0
    slots = n*2


    while k <= n:        
        if counter == slots:
            break

    
        if counter == 0:
            current = list(piso)
            current[counter] = str(mass_value)
    
            current ="".join(current)
            matriz = matriz + current
        

        else:
            current = list(piso)
            current[counter] = str(mass_value)
    
            current ="".join(current)
            matriz = matriz + current

        counter = counter + 2

        k = k + 1
    
    
    matriz = matriz[:-1]
    matriz = numpy.matrix(matriz)
    matriz_masa = matriz
    #print(matriz)


    
    c = 0
    piso = ''

    while c<= n-1:
        if c == n-1:
            piso = piso + '0'
            break
        piso = piso  + '0 '

        c = c + 1
    piso = piso + ';'
    #print(piso)


    counter = 0
    matriz = ''
    current = ''
    r = 0
    slots = n*2


    while r <= n:

        if counter == slots - 2:
            current = list(piso)
            current[counter-2] = str(k_value)
            current[counter] = str(-k_value)

            current ="".join(current)
            matriz = matriz + current
            break

    
        if counter == 0:
            current = list(piso)
            current[counter] = str(k_value *-2)
            current[counter+2] = str(k_value)
            
            current ="".join(current)
            matriz = matriz + current
        

        else:
            current = list(piso)
            current[counter-2] = str(k_value)
            current[counter] = str(k_value * -2)
            current[counter+2] = str(k_value)
            
            current ="".join(current)
            matriz = matriz + current

        counter = counter + 2

        r = r + 1
    
    matriz = matriz[:-1]
    matriz = numpy.matrix(matriz)
    matriz_k = matriz
    #print(matriz)
    #print('\n')



    

    
    eigenvalores = numpy.linalg.eigvals(numpy.linalg.inv(matriz_masa)*matriz_k)
    eigenvalores = eigenvalores.tolist()
    todos_eigenvalores.append(eigenvalores)


    n = n + 1


#Ultimo piso
frecuencias_y_axis = []
pisos_x_axis = []
cnter = 1
for i in todos_eigenvalores:

    frecuencias_y_axis.append(math.sqrt(-int(i[-1
                                               ])))
    #frecuencias.append(i[-1])
    pisos_x_axis.append(cnter)
    cnter = cnter + 1

plt.plot(pisos_x_axis, frecuencias_y_axis)
plt.show()


#Print tables in latex-format
pisos = 1
bing = ''
for i in frecuencias_y_axis:
    bing = bing + str(pisos) + '&' + str(i) + '&' + str(1/int((i+1))) +'&' + str(int(-(i**2))) + '\\\ \hline' + "\n"

    pisos = pisos + 1

print(bing)
