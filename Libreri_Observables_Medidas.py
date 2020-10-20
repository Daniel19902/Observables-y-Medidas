
import Libreria.LibreriaMatrices
import numpy as np
#--------------------drill4_1_1-----------------------------------------------------------------------------------------

def norma_vector(vector):
    return convertir_norma_vector(vector)



def convertir_norma_vector(vector):
    suma = 0
    for i in range(len(vector)):
        r = vector[i]
        for j in range(2):
            suma += r[j]**2
    return round((suma)**(1/2), 2)


def drill4_1_1(numeroEstados, ket, posicion):

    norma = norma_vector(ket)
    #probabilidad
    p = abs((complex(ket[posicion][0], ket[posicion][1])**2))/(norma**2)
    return (p.real+p.imag)*100










