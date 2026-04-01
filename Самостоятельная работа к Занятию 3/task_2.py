# TODO реализовать функцию count
def count(items_list, value):
    counter = 0
    for item in items_list:
        if item == value:
            counter += 1
    return counter


list_items = [1, 2, "3", 1]
print(count(list_items, 1) == list_items.count(1))  # True
print(count(list_items, 3) == list_items.count(3))  # True
