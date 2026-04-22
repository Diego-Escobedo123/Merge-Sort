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

print(unsorted_list)

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]

unsorted_list = merge_sort(unsorted_list)

print(unsorted_list)

if unsorted_list == sorted_list:
    print("La lista está ordenada")
else:
    print("La lista no está ordenada")

