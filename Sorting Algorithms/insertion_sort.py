
def insertionSort1(n, arr):
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    # The time complexity of insertion sort is O(n^2) in the worst and average cases, and O(n) in the best case (when the array is already sorted).
    # The space complexity is O(1) because it only requires a constant amount of additional space.
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
    return arr

print(insertionSort1(5, [2, 1, 3, 1, 2]))