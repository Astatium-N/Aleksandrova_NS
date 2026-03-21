list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_num = list_numbers[0]
max_i = 0
for i in range(len(list_numbers)):
    if list_numbers[i] >= max_num:
        max_num = list_numbers[i]
        max_i = i
last_i = len(list_numbers) - 1
temp = list_numbers[max_i]
list_numbers[max_i] = list_numbers[last_i]
list_numbers[last_i] = temp

# TODO Поменяйте местами значения согласно условию

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
