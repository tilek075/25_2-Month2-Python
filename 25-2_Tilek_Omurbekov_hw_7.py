def binary_search(my_list, val):
    n = len(my_list)
    result_ok = False
    first = 0
    last = n
    middle = 0
    result = 0
    while first < last:
        middle = (first + last) // 2
        if val == my_list[middle]:
            result_ok = True
            break
        elif val > my_list[middle]:
            first = middle
        elif val < my_list[middle]:
            last = middle
    if result_ok:
        result = f'Элемент найден "{my_list[middle]}"'
    elif not result_ok:
        result = 'Элемент не найден'
    return result


a = [1, 2, 3, 4, 5, 8, 11, 30, 99]
b = 11
print(binary_search(a, b))


def bubble_sort(unsort_list):
    n = 1
    while n < len(unsort_list):
        for i in range(len(unsort_list) - n):
            if unsort_list[i] > unsort_list[i + 1]:
                unsort_list[i], unsort_list[i + 1] = unsort_list[i + 1], unsort_list[i]
        n += 1
    return unsort_list


a = [2, 4, 10, 1, 9, 8]

print(a)
print(bubble_sort(a))
