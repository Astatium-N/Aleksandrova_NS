print("Приложение по расчёту индекса массы тела.")
print()
import time
current_year = time.localtime().tm_year

imt_n = {
    (19, 24): {"М": (20, 25), "Ж": (19, 24)},
    (25, 34): {"М": (21, 26), "Ж": (20, 25)},
    (35, 44): {"М": (22, 27), "Ж": (21, 26)},
    (45, 54): {"М": (23, 28), "Ж": (22, 27)},
    (55, 64): {"М": (24, 29), "Ж": (23, 28)},
    (65, 150): {"М": (25, 30), "Ж": (24, 29)}
}

while True:
    year_p = input("Введите год рождения: ").strip()
    try:
        year_p = int(year_p)
        if year_p < 0:
            print("Ошибка! Год не может быть отрицательным.")
        else:
            age_p = current_year - year_p
            if 19 > age_p or age_p > 150:
                print("К сожалению, Ваш возраст не подходит для расчёта. Попробуйте другой вариант.")
            else:
                break
    except ValueError:
        print("Ошибка! Год введён некорректно.")

while True:
    gen_p = input("Выберите пол (М/Ж): ").strip().upper()
    if gen_p in ("М"):
        break
    elif gen_p in ("Ж"):
        break
    else:
        print("Ошибка! Пожалуйста, введите М или Ж.")

while True:
    l_p = input("Введите рост (см): ").strip().replace(",", ".")
    try:
        l_p = float(l_p)
        if l_p < 0:
            print("Ошибка! Рост не может быть отрицательным.")
        else:
            l_p1 = (l_p / 100) * (l_p / 100)
            break
    except ValueError:
        print("Ошибка! Рост введён некорректно.")

while True:
    w_p = input("Введите вес (кг): ").strip().replace(",", ".")
    try:
        w_p = float(w_p)
        if w_p < 0:
            print("Ошибка! Вес не может быть отрицательным.")
        else:
            break
    except ValueError:
        print("Ошибка! Вес введён некорректно.")

imt_p = w_p / l_p1

for age_range, imt_data in imt_n.items():
    min_age, max_age = age_range
    if min_age <= age_p <= max_age:
        min_imt, max_imt = imt_data[gen_p]
        if min_imt <= imt_p <= max_imt:
            print("Вес в норме.")
        elif imt_p < min_imt:
            add_w = (min_imt - imt_p) * l_p1
            w_n = w_p + add_w
            print(f"Недостаточный вес, до нормы необходимо добавить вес на {add_w:.2f} кг до {w_n:.2f} кг.")
        elif imt_p > max_imt:
            add_w = (imt_p - max_imt) * l_p1
            w_n = w_p - add_w
            print(f"Избыточный вес, до нормы необходимо уменьшить вес на {add_w:.2f} кг до {w_n:.2f} кг.")
