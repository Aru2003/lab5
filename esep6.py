def is_sorted(lst):
    if lst == sorted(lst):
        return True
    elif lst == sorted(lst, reverse=True):
        return True
    else:
        return False
lst = input("Введите последовательность чисел для списка через запятую: ")
lst = lst.split(",")

# Преобразуем все элементы списка из строк в числа
lst = [int(i) for i in lst]

# Проверяем, отсортирован ли список изначально, и выводим сообщение на экран
if is_sorted(lst):
    print("Список отсортирован.")
else:
    print("Список не отсортирован.")
    