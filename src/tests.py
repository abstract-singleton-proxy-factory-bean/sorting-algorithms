import unittest
from random import randint
from algorithms import bubble_sort, radix_sort, insertion_sort


def generate_random_list() -> list:
    source = [randint(0, 1000) for _ in range(1_000)]
    sorted = [*source]
    sorted.sort()

    return [source, sorted]


class AlgorithmTest:
    class AlgorithmTest(unittest.TestCase):
        algorithm = None
        algorithm_name = None

        def test_algorithm(self):
            [source, sorted] = generate_random_list()

            response = self.algorithm.__func__(source)

            assert (
                response == sorted
            ), f"{self.algorithm_name} failed, lists are not equal"


class BubbleSortTest(AlgorithmTest.AlgorithmTest):
    algorithm = bubble_sort
    algorithm_name = "Bubble sort"


class RadixSortTest(AlgorithmTest.AlgorithmTest):
    algorithm = radix_sort
    algorithm_name = "Radix sort"


class InsertionSortTest(AlgorithmTest.AlgorithmTest):
    algorithm = insertion_sort
    algorithm_name = "Insertion sort"


if __name__ == '__main__':
    unittest.main(verbosity=3)
