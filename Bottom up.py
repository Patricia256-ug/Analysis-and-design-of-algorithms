def fibonacci_bottom_up(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

# Example
print(fibonacci_bottom_up(5))  # Output: 5
