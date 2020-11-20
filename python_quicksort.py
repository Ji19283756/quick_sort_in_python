from random import shuffle, randrange


def quicksort_pass(temp_list):
    if len(temp_list) == 1:
        return temp_list

    pivot_point = temp_list[randrange(0, len(temp_list) - 1)]
    same_as_pivot = [pivot_point]

    temp_list.remove(pivot_point)
    less_than_pivot = []
    more_than_pivot = []

    for value in temp_list:
        if value < pivot_point:
            less_than_pivot += [value]
        elif value > pivot_point:
            more_than_pivot += [value]
        elif value == pivot_point:
            same_as_pivot += [value]

    if len(less_than_pivot) > 1:
        less_than_pivot = quicksort_pass(less_than_pivot)

    if len(more_than_pivot) > 1:
        more_than_pivot = quicksort_pass(more_than_pivot)

    return less_than_pivot + same_as_pivot + more_than_pivot


thing = list(range(100))

shuffle(thing)
print(quicksort_pass(thing))