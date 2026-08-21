import random
import time


def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        if arr[high] == arr[low]:
            break

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():
    sizes = [1000, 5000, 10000, 50000, 100000]

    print(f"{'Size':>10} {'IS Time(ms)':>14} {'BS Time(ms)':>14} {'IS Comp':>10} {'BS Comp':>10}")
    print("-" * 70)

    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = random.choice(arr)

        start = time.perf_counter()
        idx1, comp1 = interpolation_search(arr, target)
        is_time = (time.perf_counter() - start) * 1000

        start = time.perf_counter()
        idx2, comp2 = binary_search(arr, target)
        bs_time = (time.perf_counter() - start) * 1000

        print(f"{size:>10} {is_time:>14.4f} {bs_time:>14.4f} {comp1:>10} {comp2:>10}")


if __name__ == "__main__":
    arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
    target = 35

    index, comparisons = interpolation_search(arr, target)

    print("Array:", arr)
    print("Target:", target)

    if index != -1:
        print("Element found at index:", index)
    else:
        print("Element not found")

    print("Comparisons:", comparisons)
    print()

    performance_analysis()
