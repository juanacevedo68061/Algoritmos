def knapsack(peso, W, valor):
    dp = [0] * (W + 1)
    
    for j in range(len(peso)):

        print('\n')
        N=W - peso[j]        
        print(f'j: {j}   N: {N}')
        x = N

        for i in range(W, peso[j]-1,-1): #peso[j]-1 es solo porque funciona asi el range para que vaya hasta peso[j]
            print(dp)
            print(f'x: {x}    i: {i}')
            
            dp[i] = max(dp[i], valor[j] + dp[x])
            x-=1

    return dp[W]

if __name__ == "__main__":
    peso = [6, 3]
    valor = [25, 15]
    print(knapsack(peso, 9, valor))
