def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list, 0
    mid = len(my_list) // 2
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    return sort_count(left[0], right[0], left[1] + right[1])

def sort_count(list_1, list_2, count = 0):
    len_1 = len(list_1)
    len_2 = len(list_2)

    i = 0
    j = 0

    res = []

    while i < len_1 and j < len_2:
        if list_2[j] < list_1[i]:
            res.append(list_2[j])
            j += 1
            count += len_1 - i

        else:
            res.append(list_1[i])
            i += 1

    while i < len_1:
        res.append(list_1[i])
        i += 1
    while j < len_2:
        res.append(list_2[j])
        j += 1

    return res, count


a_list = [5,4,3,2,1,0]
a_list = [2,4,1,3,5]
max_invert = merge_sort(a_list)

print(max_invert)