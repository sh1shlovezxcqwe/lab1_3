def count_common_elements(*lists):

    if len(lists) < 2:
        return 0

    # Преобразуем первый список в множество
    common = set(lists[0])

    # Находим пересечение со всеми остальными списками
    for lst in lists[1:]:
        common = common & set(lst)

    return len(common)


# Простые примеры использования
if __name__ == "__main__":
    # Пример 1
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    list3 = [4, 5, 6, 7]

    result = count_common_elements(list1, list2, list3)
    print(f"Пример 1: {result}")  # Выведет: 1 (только цифра 4)