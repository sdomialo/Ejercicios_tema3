import sys
from Factorial import Factorial

def main():
    num_factorial = int(input("Ingrese un número para calcular el factorial: "))

    num_fibonacci = int(input("Ingrese un número para calcular la secuencia de Fibonacci: "))

    factorial = Factorial(num_factorial)
    print(factorial)
    print("Este es Factorial Recursivo " + str(factorial.factorial_recursivo()))
    print("Este es Factorial Iterativo " + str(factorial.factorial_iterativo()) + "\n")

if __name__ == "__main__":
    main()

  