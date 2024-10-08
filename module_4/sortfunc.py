# СОРТИРОВКИ
#
#
nums = [9, 7, 6, 5, 3, 2, 1, 8, 0, 4, 1, 11]
#
# 1. Пузырьком
#
def bubble_sort(ls) :  #
    swapped = True  # если swapped = False , значит уже отсортировано (в последнем цикле не было перестановок)
    while swapped :  # цикл "пока swapped = True". Пока есть перестановки
        swapped = False  # пока перестановок не было
        for i in range(len(ls) - 1) : # -1, т.к. предпоследний и последний элементы, обрабатываются в одном, последнем цикле
            if ls[i] > ls[i + 1] : #
                ls[i], ls[i + 1] = ls[i + 1], ls[i]  #
                swapped = True  # была перестановка (ставим "флаг")
#
#print(bubble_sort(nums)) # ТАК - ничего не будет, выдаст NONE т.к. print сработает до того, как заполнится массив nume
bubble_sort(nums)  # заполнение сортированного массива
print(nums)
#
#
# 2. Выборкой
def selection_sort(ls) :  #
    for i in range(len(ls)) : # перебор всего списка
        lowest = i  # считаем первый элемент - наименьшим
        for j in range(i + 1, len(ls)) :  # перебор списка после элемента i
            if ls[j] < ls[lowest]:  # если какой то элемент меньше наименьшего,
                lowest = j  # то наименьшим становится он.
        ls[i], ls[lowest] = ls[lowest], ls[i]  #
#
selection_sort(nums)  # заполнение сортированного массива
print(nums)
#
#  конец задания
#