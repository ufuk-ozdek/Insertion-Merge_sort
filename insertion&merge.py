

list_1 = [8, 2, 4, 9, 3, 6, 1, 13, 83, 10, 17, 21, 93, 12]

"""binary insertion sort"""


def binary_insertion_sort(arr):
    key = 0
    for i in arr[1: len(arr)]:
        key += 1
        left_half = 0
        right_half = key-1
        while right_half >= left_half:
            mid = (left_half + right_half) // 2
            if arr[mid] < arr[key]:
                left_half = mid + 1
            elif arr[mid] > arr[key]:
                right_half = mid - 1
            else:
                arr = arr[:mid] + [i] + arr[mid:key] + arr[key+1:]
                break
            if left_half > right_half:
                arr = arr[:left_half] + [i] + arr[left_half:key] + arr[key+1:]
                break
    return arr


"""insertion sort"""


def insertion_sort(arr):
    key = 0
    while key < len(arr):
        x = key
        while arr[x] < arr[x-1]:
            arr[x], arr[x-1] = arr[x-1], arr[x]
            if x >= 2:
                x += -1
        key += 1
    return arr


"""merge sort"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        list_2 = arr[:mid]
        list_3 = arr[mid:]
        merge_sort(list_2)
        merge_sort(list_3)
        i = j = k = 0
        while i < len(list_2) and j < len(list_3):
            if list_2[i] > list_3[j]:
                arr[k] = list_3[j]
                j += 1
            else:
                arr[k] = list_2[i]
                i += 1

            k += 1

        while i < len(list_2):
            arr[k] = list_2[i]
            i = i + 1
            k = k + 1

        while j < len(list_3):
            arr[k] = list_3[j]
            j = j + 1
            k = k + 1

    return arr


print(merge_sort(list_1))

print(binary_insertion_sort(list_1))

print(insertion_sort(list_1))
