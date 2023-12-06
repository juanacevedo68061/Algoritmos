# kadane.py

def kadane(A):
    sum=0
    resp=0
    for i in range(0, len(A)):
        print(f'sum: {sum}      resp: {resp}')
        print(f'sum = max({sum} + {A[i]},{A[i]}) = {max(sum + A[i], A[i])}')
        sum = max(sum + A[i], A[i])
        print(f'resp = max({resp},{sum}) = {max(resp, sum)}')
        resp = max(resp, sum)
        print("\n")

    return resp

if __name__ == "__main__":
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    resultado = kadane(A)
    print("La suma máxima de la subcadena es:", resultado)
