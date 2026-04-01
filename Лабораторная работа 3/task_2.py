# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, sep=','):
    group1_list = group1.split(sep)
    group2_list = group2.split(sep)
    common_participants = set(group1_list) & set(group2_list)
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
common = find_common_participants(participants_first_group, participants_second_group, '|')
print(f"Общие участники: {common}")
