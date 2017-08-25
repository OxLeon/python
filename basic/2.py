# Definición de funciones
# 
# Creamos una funcion que escriba la seriede Fibonacci hasta n
# 
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()

fib(2000)
