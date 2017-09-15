# Definición de funciones
# 
# Creamos una funcion que escriba la seriede Fibonacci hasta n
# def es palabra reservada para definir funiones

# La forma que se almacenan las variables en Python.
# La ejecución de una función introduce una nueva tabla de símbolos usada para las variables locales de la función.
# Más precisamente, todas las asignaciones de variables en la función almacenan el valor en la tabla de símbolos local;
# así mismo la referencia a variables primero mira la tabla de símbolos local, luego en la tabla de símbolos local de las funciones
# externas, luego la tabla de símbolos global, y finalmente la tabla de nombres predefinidos. Así, no se les puede asignar
# directamente un valor a las variables globales dentro de una función (a menos se las nombre en la sentencia global),
# aunque si pueden ser referenciadas.
#
# En realidad sería un procedimiento
def fib(n):
    """Escribe la serie de Fibonacci hasta n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()

fib(2000)

def fib2(n):
    """Escribe la serie de Fibonacci hasta n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print('---------------------------')
fib100 = fib2(100)
print(fib100)

#  Funcion con valores pordefault
#  introduce la palabra reservada in, la cual prueba si una secuencia contiene o no un determinado valor.
def pedir_confirmacion(prompt, reintentos=4, recordatorio='Por favor, intente nuevamente!'):
    while True:
        ok = input(prompt)
        if ok in ('s', 'S', 'si', 'Si', 'SI'):
            return True
        if ok in ('n', 'no', 'No', 'NO'):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            raise ValueError('respuesta de usuario inválida')
        print(recordatorio)

print('---------------------------')
# Funciones con argumentos de palabra clave
def loro(tension, estado='muerto', accion='explotar', tipo='Azul Nordico'):
    print("-- Este loro no va a", accion, end=' ')
    print("si le aplicás", tension, "voltios.")
    print("-- Gran plumaje tiene el", tipo)
    print("-- Está", estado, "!")

loro(1000)                                          # 1 argumento posicional
loro(tension=1000)                                  # 1 argumento nombrado
loro(tension=1000000, accion='VOOOOOM')             # 2 argumentos nombrados
loro(accion='VOOOOOM', tension=1000000)             # 2 argumentos nombrados
loro('un millón', 'despojado de vida', 'saltar')    # 3 args posicionales
loro('mil', estado='viendo crecer las flores desde abajo')  # uno y uno

# loro()                      # falta argumento obligatorio
# loro(tension=5.0, 'muerto') # argumento posicional luego de uno nombrado
# loro(110, tension=220)      # valor duplicado para el mismo argumento
# loro(actor='Juan Garau')    # nombre del argumento desconocido
# En una llamada a una función, los argumentos nombrados deben seguir a los argumentos posicionales. Cada uno de los
# argumentos nombrados pasados deben coincidir con un argumento aceptado por la función (por ejemplo, actor no es un
# argumento válido para la función loro), y el orden de los mismos no es importante. Esto también se aplica a
# los argumentos obligatorios (por ejemplo, loro(tension=1000) también es válido). Ningún argumento puede recibir más de un
# valor al mismo tiempo. Aquí hay un ejemplo que falla debido a esta restricción:
