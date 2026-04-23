from merge_of_two_lists import merge_two_lists

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge_two_lists(left_sorted, right_sorted)

unsorted_list = [8, 4, 1, 3, 7, 2, 5, 6]
expected = [1, 2, 3, 4, 5, 6, 7, 8]

result = merge_sort(unsorted_list)

print("Resultado:", result)

if result == expected:
    print("Test PASÓ")
else:
    print("Test FALLÓ")