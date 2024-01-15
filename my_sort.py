import timeit
import random


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def test_algorithm(algorithm, data):
    setup_code = f"from __main__ import {algorithm}"
    stmt = f"{algorithm}({data})"
    time = timeit.timeit(stmt, setup=setup_code, number=100)
    return time


def main():
    data_sizes = [10, 100, 1000, 10000]

    for size in data_sizes:
        data = [random.randint(1, 1000) for _ in range(size)]
        copy = data.copy()
        merge_sort_time = timeit.timeit(lambda: merge_sort(copy), number=1)
        copy = data.copy()
        insertion_sort_time = timeit.timeit(lambda: merge_sort(copy), number=1)
        copy = data.copy()
        timsort_time = timeit.timeit(lambda: copy.sort(), number=1)

        print(f"\nData Size: {size}")
        print(f"Merge Sort Time: {merge_sort_time:.3f}")
        print(f"Insertion Sort Time: {insertion_sort_time:.3f}")
        print(f"Timsort Time: {timsort_time:.5f}")


if __name__ == "__main__":
    main()