"""
Bubble Sort and Selection Sort.

Classical sorting algorithms comparing adjacent and minimum elements.
"""


def bubble_sort(arr: list[int]) -> list[int]:
    """In-place optimized Bubble Sort."""
    n = len(arr)
    data = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data


def selection_sort(arr: list[int]) -> list[int]:
    """Selection Sort by repeatedly finding minimum element."""
    data = arr.copy()
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data


if __name__ == "__main__":
    print("=== Comparison Sorting Algorithms ===")
    sample = [64, 25, 12, 22, 11]
    print(f"Raw Array      : {sample}")
    print(f"Bubble Sorted   : {bubble_sort(sample)}")
    print(f"Selection Sorted: {selection_sort(sample)}")
