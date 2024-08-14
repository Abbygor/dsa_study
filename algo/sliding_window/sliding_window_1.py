"""
Maximum Sum of K continuous elements

Ex:
    arr = [12,20,34,13,45,50]
    k = 3
    res = 108 -> sum[13,45,50]

    1. Initialize the maxSum and currentSum to the sum of the first K elements of the array
    2. Initialize the l (left) pointer that keep tracks the elemento to rest
    3. Iterate until len(arr) - k to avoid index out of range
    4. The currentSum must be equal to add the next element (arr[r + k]) and rest the previous element (arr[l])
        currentSum = sum(arr[12,20,34]) = 66
        -> then in the next iteration we must add 13 and rest 12
        66 + arr[0 + 3] - arr[0] -> 66 + 13 - 12 = 67
        -> the next iteration
        67 + arr[1 + 3] - arr[1] -> 67 + 45 - 20 = 92
        -> the next iteration
        92 + arr[2 + 3] - arr[2] -> 92 + 50 - 34 = 108

        
Time Complexy: O(n)
Space Complexy: O(1)
"""

def sliding_window(arr, k):
    maxSum = float('-inf')
    currentSum = 0
    l = 0
    for r in range(len(arr)):
        currentSum += arr[r]
        if (r - l == k - 1):
            maxSum = max(maxSum, currentSum)
            currentSum -= arr[l]
            l += 1
    return maxSum

def sliding_window_pythonic(arr, k):
    maxSum = sum(arr[:k])
    currentSum = maxSum
    l = 0
    for r in range(len(arr) - k):
        currentSum += arr[r+k] - arr[l]
        maxSum = max(maxSum, currentSum)
        l += 1
    return maxSum
    


arr = [12,20,34,13,45,50]
k = 3

print(sliding_window(arr, k))
