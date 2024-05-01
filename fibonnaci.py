class Fibonacci:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "Fibonacci de " + str(self.n)

    def get_n(self):
        return self.n

    def set_n(self, n):
        self.n = n

    def fibonacci_iterativo(self):
        if self.n <= 0:
            return []
        elif self.n == 1:
            return [0]
        elif self.n == 2:
            return [0, 1]
        else:
            fib_sequence = [0, 1]
            for i in range(2, self.n):
                fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
            return fib_sequence

    def fibonacci_recursivo(self):
        if self.n <= 0:
            return []
        elif self.n == 1:
            return [0]
        elif self.n == 2:
            return [0, 1]
        else:
            fib_sequence = self.fibonacci_recursivo_helper(self.n)
            return fib_sequence

    def fibonacci_recursivo_helper(self, n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib_sequence = self.fibonacci_recursivo_helper(n-1)
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
            return fib_sequence


def main():
    fibonacci = Fibonacci(0)
    n = int(input("Ingrese un numero para calcular la secuencia de Fibonacci: "))
    fibonacci.set_n(n)
    print(fibonacci)
    print("Esta es la secuencia de Fibonacci de forma recursiva: " + str(fibonacci.fibonacci_recursivo()))
    print("Esta es la secuencia de Fibonacci de forma iterativa: " + str(fibonacci.fibonacci_iterativo()))