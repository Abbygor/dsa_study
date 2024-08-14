def prefix_sum_in_place(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

def prefix_sum_new_array(arr):
    res = []
    res.append(arr[0])
    for i in range(1, len(arr)):
        res.append(arr[i] + res[i-1])
    return res

arr = [1, 2, 3, 4, 5, 6, 7]

print(prefix_sum_new_array(arr))
prefix_sum_in_place(arr)
print(arr)