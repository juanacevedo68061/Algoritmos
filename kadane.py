# kadane.py

def kadane(A):
    suma_temporal=0
    suma_maxima=0
    for i in range(0, len(A)):
        print(f'suma_temporal: {suma_temporal}      suma_maxima: {suma_maxima}')
        print(f'suma_temporal = max({suma_temporal} + {A[i]},{A[i]}) = {max(suma_temporal + A[i], A[i])}')
        
        suma_temporal = max(suma_temporal + A[i], A[i])
        
        print(f'suma_maxima = max({suma_maxima},{suma_temporal}) = {max(suma_maxima, suma_temporal)}')
        suma_maxima = max(suma_maxima, suma_temporal)
        print("\n")

    return suma_maxima

if __name__ == "__main__":
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    resultado = kadane(A)
    print("La suma máxima de la subcadena es:", resultado)
