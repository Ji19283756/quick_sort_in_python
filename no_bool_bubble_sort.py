def no_bool_bubble_sort(unsorted_list):
    for y in range(1, len(unsorted_list) - 1):
        for x in range(len(unsorted_list) - y):
            try:
                value = \
                    (((unsorted_list[x] - unsorted_list[x + 1]) // abs(
                        unsorted_list[x + 1] - unsorted_list[x])) + 1) // 2
                unsorted_list[x], unsorted_list[x + 1] = unsorted_list[x + value], unsorted_list[x + 1 - value]
            except ZeroDivisionError:
                pass

    return unsorted_list
    
    
