import cmath

# сложение значений
def add(a, b):
    return a + b

# умножение значений
def mult(a, b):
    return a * b

<<<<<<< HEAD
# проверка
print(complex_operation('5+2j', '3-1j', '*'))
=======
# вычитание значений
def diff(a, b):
    return a - b

 # деление значений
def div(a, b):
    if not b:
        return 'Деление на ноль'
    return a / b

# возведение в степерь значений
def power(a, n):
    return a ** n

# извлечение корня в степени (a)
def sqrt(a):
    b = cmath.sqrt(a)
    if not b.imag:
        return b.real
    return b
>>>>>>> 2d5e753340bd17c2342d1b438b8a9d5e647e2934
