
"""binary insertion sort"""


def binary_insertion_sort(arr):
    key = 0
    for i in arr[1: len(arr)]:
        key += 1
        left_half = 0
        right_half = key - 1
        while right_half >= left_half:
            mid = (left_half + right_half) // 2
            if arr[mid] < arr[key]:
                left_half = mid + 1
            elif arr[mid] > arr[key]:
                right_half = mid - 1
            else:
                arr = arr[:mid] + [i] + arr[mid:key] + arr[key + 1:]
                break
            if left_half > right_half:
                arr = arr[:left_half] + [i] + arr[left_half:key] + arr[key + 1:]
                break
    return arr


"""insertion sort"""


def insertion_sort(arr):
    key = 1
    while key < len(arr):
        index = key
        while arr[index] < arr[index - 1]:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            if index >= 2:
                index += -1
        key += 1
    return arr


"""merge sort"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        first_part = arr[:mid]
        second_part = arr[mid:]
        merge_sort(first_part)
        merge_sort(second_part)
        first_index = second_index = sorted_index = 0
        while first_index < len(first_part) and second_index < len(second_part):
            if first_part[first_index] > second_part[second_index]:
                arr[sorted_index] = second_part[second_index]
                second_index += 1
            else:
                arr[sorted_index] = first_part[first_index]
                first_index += 1

            sorted_index += 1

        while first_index < len(first_part):
            arr[sorted_index] = first_part[first_index]
            first_index = first_index + 1
            sorted_index = sorted_index + 1

        while second_index < len(second_part):
            arr[sorted_index] = second_part[second_index]
            second_index = second_index + 1
            sorted_index = sorted_index + 1

    return arr


num_list = [8, 2, 4, 9, 3, 6, 1, 13, 83, 10, 17, 21, 93, 12]
print(merge_sort(num_list))

print(binary_insertion_sort(num_list))

print(insertion_sort(num_list))
