def fibonacci(n):
    """
    Calcula el n-ésimo número de Fibonacci.
    Args:
        n (int): Posición en la secuencia (empezando por 0).
    Returns:
        int: El n-ésimo número de Fibonacci.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Uso
for i in range(10):
    print(fibonacci(i), end=" ")
# 0 1 1 2 3 5 8 13 21 34
