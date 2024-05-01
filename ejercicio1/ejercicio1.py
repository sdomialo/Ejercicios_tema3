import random
import time

def bucket_sort(arr):
    pass

def shell_sort(arr):
    pass

def radix_sort(arr):
    pass

sizes = [100000, 1000000, 10000000]
lists = []

for size in sizes:
    random_list = [random.randint(0, 1000000) for _ in range(size)]
    lists.append(random_list)

for i, lst in enumerate(lists):
    print(f"Lista de tamaño {sizes[i]}:")
    
    start_time = time.time()
    bucket_sort(lst)
    end_time = time.time()
    print(f"Tiempo de ejecución de bucket sort: {end_time - start_time} segundos")
    
    start_time = time.time()
    shell_sort(lst)
    end_time = time.time()
    print(f"Tiempo de ejecución de shell sort: {end_time - start_time} segundos")
    
    start_time = time.time()
    radix_sort(lst)
    end_time = time.time()
    print(f"Tiempo de ejecución de radix sort: {end_time - start_time} segundos")