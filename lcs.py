# Contenido de lcs.py

def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    
    dp = [0] * (n + 1)
    
    for i in range(1, m + 1):
        prev = 0
        for j in range(1, n + 1):
            current = dp[j]
            if X[i - 1] == Y[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = current
    
    return dp[n]

# Ejemplo de uso
if __name__ == "__main__":
    X = "ABCBDAB"
    Y = "BDCAB"
    result = lcs_length(X, Y)
    print("Longitud de la subsecuencia común más larga:", result)
