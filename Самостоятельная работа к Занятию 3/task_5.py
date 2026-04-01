def delete(list_, index=None):
    # TODO реализовать функцию удаления элемента из списка по индексу
    new_list = list_.copy()
    if index is None:
        new_list.pop()
    else:
        new_list.pop(index)
    return new_list

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
