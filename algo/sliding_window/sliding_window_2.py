"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Ex:
    arr = [2,3,1,2,4,3]
    target = 7
    res = 7 -> sum[4,3]

    1. Initialize the minSize to a very high number and currentSum to 0
    2. Initialize the l (left) pointer that keep tracks the element to rest
    3. Iterate from 0 until len(arr)
    4. Add nums[r] to the currentSum
        currentSum += nums[0] -> 0 += 2 = 2
        -> next iteration
        currentSum += nums[1] -> 2 += 3 = 5
        -> next iteration
        currentSum += nums[2] -> 5 += 1 = 6
        -> next iteration
        currentSum += nums[3] -> 6 += 2 = 8
            While currentSum >= target:
            -> first iteration
            minSize = min(float('inf), 3 - 0 + 1) = 4
            currentSum -= nums[l] -> 8 - 2 = 6
        -> next iteration
        currentSum += nums[4] -> 6 += 4 = 10
            While currentSum >= target:
            -> first iteration
            minSize = min(4, 4 - 1 + 1) = 4
            currentSum -= nums[l] -> 10 - 3 = 7
            -> second iteration
            minSize = min(4, 4 - 2 + 1) = 3
            currentSum -= nums[l] -> 7 - 1 = 6
        -> next iteration
        currentSum += nums[5] -> 6 += 3 = 9
            While currentSum >= target:
            -> first iteration
            minSize = min(3, 5 - 3 + 1) = 3
            currentSum -= nums[l] -> 9 - 2 = 7
            -> second iteration
            minSize = min(3, 5 - 4 + 1) = 2 <----------- res
            currentSum -= nums[l] -> 7 - 4 = 3

Time Complexy: O(n)
Space Complexy: O(1)
"""

def sliding_window(nums, target):
    minSize = float('inf')
    currentSum = 0
    l = 0
    for r in range(len(nums)):
        currentSum += nums[r]
        while currentSum >= target:
            minSize = min(minSize, r - l + 1)
            currentSum -= nums[l]
            l += 1
    if minSize == float('inf'):
        return 0
    return minSize

nums = [2,3,1,2,4,3]
target = 7

print(sliding_window(nums, target))