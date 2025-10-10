from lib import count_common_elements

def test_count_common_elements():
    """Тестирование функции count_common_elements"""

    # Тест 1: Обычные списки с общими элементами
    assert count_common_elements([1, 2, 3], [2, 3, 4]) == 2
    print("✓ Тест 1 пройден: [1,2,3] и [2,3,4] → 2 общих элемента")

    # Тест 2: Нет общих элементов
    assert count_common_elements([1, 2], [3, 4]) == 0
    print("✓ Тест 2 пройден: [1,2] и [3,4] → 0 общих элементов")

    # Тест 3: Три списка
    assert count_common_elements([1, 2, 3], [2, 3, 4], [3, 4, 5]) == 1
    print("✓ Тест 3 пройден: три списка → 1 общий элемент")

    # Тест 4: Пустые списки
    assert count_common_elements([]) == 0
    print("✓ Тест 4 пройден: пустой список → 0")

    # Тест 5: Дубликаты в списках
    assert count_common_elements([1, 2, 2, 3], [2, 3, 3, 4]) == 2
    print("✓ Тест 5 пройден: списки с дубликатами → 2 общих элемента")

    # Тест 6: Один список
    assert count_common_elements([1, 2, 3]) == 3
    print("✓ Тест 6 пройден: один список → все элементы")

    print("\n🎉 Все тесты пройдены успешно!")

if __name__ == "__main__":
    test_count_common_elements()
