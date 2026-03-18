x = 1
y = -1

# TODO переписать через if-elif-else
if x > 0 and y > 0:
    print("Первая четверть")
elif x < 0 and y > 0:
    print("Вторая четверть")
elif x < 0 and y < 0:
    print("Третья четверть")
elif x > 0 and y < 0:
    print("Четвертая четверть")
else:
    print("Точка находится на оси координат")  # когда x == 0 или y == 0
