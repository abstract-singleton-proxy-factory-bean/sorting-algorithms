from itertools import chain


def flat(source: list) -> list:
    return list(chain(*source))


def get_num_digits(value: list) -> int:
    return len(str(value))


def insertion_sort(source: list):
    loop_range = len(source)
    cloned = [*source]

    for i in range(1, loop_range):
        key = cloned[i]
        j = i - 1

        while j >= 0 and cloned[j] > key:
            cloned[j + 1] = cloned[j]
            j = j - 1

        cloned[j + 1] = key

    return cloned


def radix_sort(source: list) -> list:
    maximum = max(source)
    digits = get_num_digits(maximum)

    for digit in range(digits):
        bucket = [[] for i in range(10)]

        for item in source:
            index = item // 10 ** (digit) % 10
            bucket[index].append(item)

        source = flat(bucket)

    return source


def bubble_sort(source: list) -> list:
    cloned = [*source]
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(len(cloned) - 1):
            if cloned[i] > cloned[i + 1]:
                cloned[i + 1], cloned[i] = cloned[i], cloned[i + 1]
                is_sorted = False

    return cloned
