def fibonacci_top_down(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_top_down(n-1, memo) + fibonacci_top_down(n-2, memo)
    return memo[n]

# Example
print(fibonacci_top_down(5))  # Output: 5
