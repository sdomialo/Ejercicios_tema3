class Factorial:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "Factorial de " + str(self.n)

    def get_n(self):
        return self.n

    def set_n(self, n):
        self.n = n
    
    def factorial_iterativo(self):
        result = 1
        for i in range(1, self.n+1):
            result *= i
        return result

    def factorial_recursivo(self):

        if self.n == 0:
            return 1
        else:
            return self.n * Factorial(self.n-1).factorial_recursivo()

def main():
    factorial = Factorial(0)  
    n = int(input("Ingrese un numero para calcular el factorial: "))
    factorial.set_n(n)
    print(factorial)
    print("Este es Factorial Recursivo " + str(factorial.factorial_recursivo()))
    print("Este es Factorial Iterativo " + str(factorial.factorial_iterativo()))
    