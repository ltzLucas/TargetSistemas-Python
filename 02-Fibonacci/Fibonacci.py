def sequencia_fibonacci(n):
    """Verifica se n pertence à sequência de Fibonacci."""
    if n < 0:
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

# Exemplo de uso
numero = int(input("Digite um número: "))
if sequencia_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")