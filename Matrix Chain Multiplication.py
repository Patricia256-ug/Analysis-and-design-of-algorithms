import sys

def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]

# Example
dimensions = [2, 3, 4, 5]
print(matrix_chain_order(dimensions))  # Output: 64
