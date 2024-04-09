'''Questão'''

def fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] <= n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    if n in fib_seq:
        return f"O número {n} está na sequência de Fibonacci."
    else:
        return f"O número {n} não se encontra na sequencia de Fibonacci."

numero = 21
print(fibonacci(numero))




