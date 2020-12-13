from keyboard import is_pressed
from time import sleep


def one_quicksort_pass(temp_list):
    sleep_time = 0.2
    print("\n".join(f"{number}: {value}" for number, value in enumerate(temp_list, start=1)))

    while True:
        pivot_name = input("which person is the most in the middle?\n(enter either the number or the name)\n").strip()
        try:
            if any(number in pivot_name for number in "1234567890"):
                pivot_name = temp_list[int(pivot_name) - 1]
            temp_list.remove(pivot_name)
            break
        except ValueError:
            print("that name or number isn't available!")

    less_than_pivot = []
    more_than_pivot = []
    same_than_pivot = [pivot_name]

    for value in temp_list:
        print(f"\nhigher rank than {pivot_name}: {', '.join(less_than_pivot)} ⇽ (press ,)"
              f"\nsame as {pivot_name}: {', '.join(same_than_pivot)}          ⇽ (press l) which pile should {value} go?"
              f"\nlower rank than {pivot_name}: {', '.join(more_than_pivot)}  ⇽ (press.)")

        while True:
            if is_pressed(","):
                less_than_pivot += [value]
                sleep(sleep_time)
                break
            elif is_pressed("."):
                more_than_pivot += [value]
                sleep(sleep_time)
                break
            elif is_pressed("l"):
                same_than_pivot += [value]
                sleep(sleep_time)
                break

    if len(less_than_pivot) > 6:
        less_than_pivot = one_quicksort_pass(less_than_pivot)
    else:
        less_than_pivot = insertion_sort(less_than_pivot)

    if len(more_than_pivot) > 6:
        more_than_pivot = one_quicksort_pass(more_than_pivot)
    else:
        more_than_pivot = insertion_sort(more_than_pivot)

    return less_than_pivot + same_than_pivot + more_than_pivot


def insertion_sort(temp_list: list) -> list:
    sleep_time = 0.2
    length_of_list = " " * (sum(map(len, temp_list)) - 10)
    for x in range(1, len(temp_list)):
        second_index = x
        first_index = x - 1
        pos_of_2nd_name_midpoint = sum(map(len, temp_list[first_index:second_index])) + \
                                   int(len(temp_list[second_index]) / 2)

        first_distance = sum([len(temp_list[x]) + 2 for x in range(first_index)])

        print(f"\n{', '.join(temp_list)}\n"
              f"{' ' * first_distance}↖{'-' * pos_of_2nd_name_midpoint}↩"
              f"\nhighest rank{length_of_list}lowest rank")

        while True:
            if first_index < 0 or is_pressed("."):
                sleep(sleep_time)
                break
            elif is_pressed(","):
                temp_list[first_index], temp_list[second_index] = temp_list[second_index], temp_list[first_index]
                second_index -= 1
                first_index -= 1
                sleep(sleep_time)

                pos_of_2nd_name_midpoint = sum(map(len, temp_list[first_index:second_index])) + \
                                           int(len(temp_list[second_index]) / 2)

                first_distance = sum([len(temp_list[x]) + 2 for x in range(first_index)])

                if first_index != -1:
                    print(f"\n{', '.join(temp_list)}\n"
                          f"{' ' * first_distance}↖{'-' * pos_of_2nd_name_midpoint}↩"
                          f"\nhighest rank{length_of_list}lowest rank")

    return temp_list


print("Notes: moving value1 before value2 means that value1 is higher ranked than value2")

list_to_be_ranked = ['Subway', 'Starbucks', "McDonald's", "Dunkin'",
                     'Pizza Hut', 'Burger King', "Wendy's", 'Taco Bell']

list_to_be_ranked = [name.lower().strip() for name in list_to_be_ranked]
list_to_be_ranked = insertion_sort(list_to_be_ranked)
# list_to_be_ranked = one_quicksort_pass(list_to_be_ranked)

print("\n", "\n".join(f"{x}: {value}" for x, value in enumerate(list_to_be_ranked, start=1)))
