def bubble_sort(a):
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    # The time complexity of bubble sort is O(n^2) in the worst and average cases, and O(n) in the best case (when the array is already sorted).
    # The space complexity is O(1) because bubble sort is an in-place sorting algorithm.
    flag = True
    total_count = 0
    while flag:
        count = 0
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                count+=1
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
                total_count += 1
        if count == 0:
           flag = False 
                    
    print(a)
    print(f"Array is sorted in {total_count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    return a