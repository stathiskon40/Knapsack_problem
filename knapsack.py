class item:
    def __init__(self, name, useful, weight):
        self.name = name
        self.useful = useful
        self.weight = weight


def array_init(items_array):
    dynamic_array = []
    for _ in range(0, len(items_array)+1):
        dynamic_array.append([])

    return dynamic_array


def complete_dynamic_array(items_array, dynamic_array, sack_size):
    # Complete the first row with 0
    for _ in range(0, sack_size+1):
        dynamic_array[0].append(0)

    for temp_item in range(1, len(items_array)+1):
        for temp_weight in range(0, sack_size+1):
            if (temp_weight - items_array[temp_item-1].weight) >= 0:
                dynamic_array[temp_item].append(max(dynamic_array[temp_item-1][temp_weight], dynamic_array[temp_item-1][temp_weight-items_array[temp_item-1].weight] + items_array[temp_item-1].useful))  # nopep8
            else:
                dynamic_array[temp_item].append(dynamic_array[temp_item-1][temp_weight])  # nopep8

    return dynamic_array


def choose_items(items_array, dynamic_array):
    bottom_weight = dynamic_array[len(dynamic_array)-1][len(dynamic_array[0])-1]  # nopep8
    upper_weight = dynamic_array[len(dynamic_array)-1][len(dynamic_array[0])-1]
    final_knapsack_array = []

    collumn = len(dynamic_array[0])-1

    for i in range(len(dynamic_array)-1, 0, -1):
        bottom_weight = dynamic_array[i][collumn]

        if not bottom_weight:
            break

        upper_weight = dynamic_array[i-1][collumn]

        if bottom_weight == upper_weight:
            pass
        elif not(bottom_weight == upper_weight):
            final_knapsack_array.append(items_array[i-1])
            collumn -= items_array[i-1].weight

    return final_knapsack_array


def print_array(array):
    for row in range(0, len(array)):
        for column in range(0, len(array[row])):
            print(f"{array[row][column]} ", end="")
        print("\n")


items_array = [
    item("rope", 5, 7),
    item("flashlight", 6, 6),
    item("boots", 7, 3),
    item("axe", 2, 5),
    item("tent", 8, 4)
]


sack_size = 15

dynamic_array = array_init(items_array)
complete_dynamic_array(items_array, dynamic_array, sack_size)
print_array(dynamic_array)
array = choose_items(items_array, dynamic_array)

total_weight, total_value = 0, 0
for i in array:
    total_weight += i.weight
    total_value += i.useful
    print(f"{i.name} ")
