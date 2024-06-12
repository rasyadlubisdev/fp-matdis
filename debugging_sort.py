def merge(left_half, right_half):
    result = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] > right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    result += left_half[i:]
    result += right_half[j:]
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)

arr = [90000000, 40000000, 79120000, 40000000, 0, 2976000]
print(merge_sort(arr))
