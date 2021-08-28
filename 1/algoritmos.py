'''

>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120

>>> recursivo.factorial(13)
6227020800

'''


def fibonacci(number):
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonacci(number - 1) + fibonacci(number - 2)

def palindromo(sentence):
    ''' 
    Retorna verdadero si es un palíndromo
    en caso contrario retorna falso

    sentence => string o entero

    Extended Slices   [::-1]   =>  Negative values also work to make a copy of the same list in reverse order 
    This also works for tuples, arrays, and strings

    s='abcd'
    s[::2]
        'ac'
    s[::-1]
        'dcba'

    >>> palindromo("anita lava la tina")
    True

    >>> palindromo(12321)
    True
    
    >>> palindromo("Abborgia")
    False

    ''' 

    sentence = str(sentence).lower().replace(" ", "")
    return sentence == sentence[::-1]

class Recursivo:
    def factorial(self, number):
        if number == 0: return 1
        else: return number * self.factorial(number-1)



# ejecutar todas las pruebas: (solo ejecutando por consola este archivo .py en este caso: algoritmos.py)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    doctest.testfile("test.txt")


 # python algoritmos.py -v   para hacer las pruebas!

 