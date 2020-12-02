from random import shuffle


def insertion_sort(temp_list: list) -> list:
    for x in range(1, len(temp_list)):
        second_index = x
        first_index = x-1
        while True:
            if first_index < 0:
                break
            elif temp_list[first_index] > temp_list[second_index]:
                temp_list[first_index], temp_list[second_index] = temp_list[second_index], temp_list[first_index]
                second_index -= 1
                first_index -= 1
            else:
                break

    return temp_list


list_length = 40
scrambled_list = list(range(100))
shuffle(scrambled_list)

thing = insertion_sort(scrambled_list)

print(thing)