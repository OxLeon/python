print("hola mundo desde python")
## x = int(input("Ingresa un entero, por favor: "))
x = 1
if x < 0:
    print('Negativo cambiado a cero')
elif x == 0:
    print('Cero')
elif x == 1:
    print('Simple')
else:
    print('Mas')

# Manejo de arrays

palabras = ['gato','perro','conejo','defenestrado']
for p in palabras:
    print(p, len(p))

print ('-------------')
for p in palabras[:]:  # hace una copia por rebanada de toda la lista
    if len(p) > 6:
        palabras.insert(0, p)  # list.insert(index, obj)

print(palabras)

for i in range(5):
    print(i)

# Other examples how to use range.
# 
# range(5, 10)
#    5 through 9
#
# range(0, 10, 3)
#    0, 3, 6, 9
#
# range(-10, -100, -30)
#   -10, -40, -70
#
# palabras
# if var1 >= 30:
#    print "1 - Got a true expression value"
#    print var1
# else:
#    print "1 - Got a false expression value"
#    print var1
#
# var2 = 0
# if var2:
#    print "2 - Got a true expression value"
#    print var2
# else:
#    print "2 - Got a false expression value"
#    print var2
#
# print "Good bye!"
print ('-------------')
a = ['Mary', 'tenia', 'un', 'corderito']

for i in range(len(a)):
    print(i, a[i])

# De muchas maneras el objeto devuelto por range() se comporta como si fuera una lista, pero no lo es.
# Es un objeto que devuelve los ítems sucesivos de la secuencia deseada cuando iterás sobre él, pero realmente no construye la lista,
#  ahorrando entonces espacio.
#
# Decimos que tal objeto es iterable; esto es, que se lo puede usar en funciones y construcciones que
# esperan algo de lo cual obtener ítems sucesivos hasta que se termine. Hemos visto que la declaración
# for es un iterador en ese sentido. La función list() es otra; crea listas a partir de iterables:

# BREACK, CONTINUE, ELSE en lazos
#
# else tiene más en común con el else de una declaración try que con el de un if: el else de un try
# se ejecuta cuando no se genera ninguna excepción, y el else de un ciclo se ejecuta cuando no hay ningún break.

print ('-------------')
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'es igual a', x, '*', n/x)
            break
    else:
        # sigue el bucle sin encontrar un factor
        print(n, 'es un numero primo')

# CONTINUE Continua con la siguiente interacción del ciclo
print ('-------------')
for num in range(2, 10):
    if num % 2 == 0:
        print("Encontré un número par", num)
        continue
    print("Encontré un número", num)
