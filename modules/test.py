#
nums = [9, 7, 6, 5, 3, 2, 1, 8, 0, 4, 1, 11, 23, 5, 456]
#
# 3. Вставкой - алгоритм - ГОВНО
# def insertion_sort(ls) :  #
#     for i in range(1, len(ls)) : # перебор списка, начиная с 2-го элемента
#         key = ls[i]  #
#         j = i - 1
#         #print(locals())  #
#         while ls[j] > key and j >= 0 :  #
#             ls[j + 1] = ls[j]  #
#             #print(locals())  #
#             j -= j  #
#         ls[j + 1] = key  #
#         #print(locals())  #
#     return ls
# #
# print(insertion_sort(nums)) #
# #
#
# # 3. Вставкой - ПРАВИЛЬНЫЙ АЛГОРИТМ
# #
def insertion_sort(ls):
    for i in range(len(ls)):
        cursor = ls[i]
        pos = i
        while pos > 0 and ls[pos - 1] > cursor:
            # Меняем местами число, продвигая по списку
            ls[pos] = ls[pos - 1]
            pos = pos - 1
        # Остановимся и сделаем последний обмен
        ls[pos] = cursor

    return ls
#
print(insertion_sort(nums)) #
# #