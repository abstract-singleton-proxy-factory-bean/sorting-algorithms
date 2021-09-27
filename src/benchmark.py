from random import randint
from time import perf_counter
from algorithms import radix_sort, bubble_sort, insertion_sort

source = [randint(1, 10_000) for _ in range(5_000)]

answer = [*source]
answer.sort()

for algorithm in [radix_sort, insertion_sort, bubble_sort]:
    start = perf_counter()
    algorithm_answer = algorithm(source)
    end = perf_counter()

    print(f"[{algorithm.__name__.upper()}]: {end - start:.8f}s")
