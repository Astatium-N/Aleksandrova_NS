list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

# TODO завести отдельные счетчики для четных и нечетных чисел
num1_count = 0
num2_count = 0

# TODO с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных
for num in list_:
    if num % 2 == 0:
        num1_count += 1
    elif num % 2 != 0:
        num2_count += 1
# TODO вывести каких чисел больше
if num1_count > num2_count:
    print("Четных чисел больше")
elif num1_count < num2_count:
    print("Нечетных чисел больше")
else:
    print("Четных и нечетных одинаковое количество")