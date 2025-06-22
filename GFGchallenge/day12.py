
# Maximum Circular Subarray Sum
# This code provides three different approaches to find the maximum circular subarray sum.
# Approach 1: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# This approach uses a brute force method to calculate the maximum subarray sum
# by iterating through all possible starting points and calculating the sum
# for each subarray that wraps around the end of the array.
# It maintains a variable to keep track of the maximum sum found so far.
def circularsum(arr):
    n = len(arr)
    res = arr[0]


    for i in range(n):
        currsum = 0

        for j in range(n):
            idx = (i+j) % n
            currsum += arr[idx]
            res = max(res, currsum)
    
    return res


# Approach 2: Prefix and Suffix Sums
# Time Complexity: O(n)
# Space Complexity: O(n)
# This approach calculates the maximum subarray sum in a circular manner
# by using prefix and suffix sums. It maintains a suffix sum array to
# efficiently compute the maximum subarray sum that wraps around the end of the array.
# It iterates through the array, calculating the maximum subarray sum
# for both normal and circular cases. The maximum circular subarray sum is
# derived from the prefix sum and the maximum suffix sum.   
def circularsum1(arr):
    n = len(arr)

    suffix_sum = arr[n-1]

    maxSuffix = [0] * (n+1)

    maxSuffix[n-1] = arr[n-1]

    for i in range(n-2, -1, -1):
        suffix_sum += arr[i]
        maxSuffix[i] = max(maxSuffix[i+1], suffix_sum)

    currSum = 0
    prefix_sum = 0

    circularSum = arr[0]
    normalSum = arr[0]

    for i in range(n):
        currSum += arr[i]
        normalSum = max(normalSum, currSum)

        prefix_sum += arr[i]
        circularSum = max(circularSum, prefix_sum + maxSuffix[i+1])

    return max(circularSum, normalSum)


# Approach 3: Kadane's Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
# This approach uses Kadane's algorithm to find the maximum subarray sum
# in both normal and circular cases.
# It calculates the total sum of the array, the maximum subarray sum,
# and the minimum subarray sum. The maximum circular subarray sum is then
# derived from the total sum minus the minimum subarray sum.
# This approach is efficient and works well for both positive and negative numbers.
# It handles cases where all elements are negative by checking if the minimum
# subarray sum equals the total sum, in which case it returns the normal maximum subarray sum.

def circularsum3(arr):
    totalSum = 0
    currMaxsum = 0
    currMinsum = 0
    maxSum = arr[0]
    minSum = arr[0]

    for i in range(len(arr)):
        currMaxsum = max(currMaxsum + arr[i], arr[i])
        maxSum = max(maxSum, currMaxsum)

        currMinsum = min(currMinsum + arr[i], arr[i])
        minSum = min(minSum, currMinsum)

        totalSum += arr[i]

    normalSum = maxSum
    circularSum = totalSum - minSum

    if minSum == totalSum: # for all negative numbers
        return normalSum
    
    return max(normalSum, circularSum)