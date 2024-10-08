#
nums = [9, 7, 6, 5, 3, 2, 1, 8, 0, 4, 1, 11, 23, 5, 456]
#
# 3. Вставкой
def insertion_sort(ls) :  #
    for i in range(1, len(ls)) : # перебор списка, начиная с 2-го элемента
        key = ls[i]  #
        j = i - 1
        #print(locals())  #
        while ls[j] > key and j >= 0 :  #
            ls[j + 1] = ls[j]  #
            #print(locals())  #
            j -= j  #
        ls[j + 1] = key  #
        #print(locals())  #
    return ls
#
print(insertion_sort(nums)) #
#
#