# kadane.py

def kadane(arr):
    max_actual = max_global = arr[0]

    for i in range(1, len(arr)):
        max_actual = max(arr[i], max_actual + arr[i])
        if max_actual > max_global:
            max_global = max_actual

    return max_global

if __name__ == "__main__":
    # Ejemplo de uso:
    mi_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    resultado = kadane(mi_array)
    print("La suma máxima de la subcadena es:", resultado)
