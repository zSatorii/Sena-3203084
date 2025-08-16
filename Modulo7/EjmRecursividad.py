def factorial(n):
    """
    Calcula el factorial de un número.
    Args:
        n (int): Número entero positivo.
    Returns:
        int: El factorial de n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Uso
print(factorial(5))  # 120
