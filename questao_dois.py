def fibonacci(numero):
    a = 0
    b = 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return True
    else:
        return False

numero_digitado = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if fibonacci(numero_digitado):
    print(f"{numero_digitado} pertence à sequência de Fibonacci.")
else:
    print(f"{numero_digitado} não pertence à sequência de Fibonacci.")
