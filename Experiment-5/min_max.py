def min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        return arr[high], arr[low]

    mid = (low + high) // 2

    left_min, left_max = min_max(arr, low, mid)
    right_min, right_max = min_max(arr, mid + 1, high)

    return min(left_min, right_min), max(left_max, right_max)


arr = [12, 45, 7, 89, 23, 56, 91, 3, 18]

minimum, maximum = min_max(arr, 0, len(arr) - 1)

print("Array:", arr)
print("Minimum:", minimum)
print("Maximum:", maximum)
