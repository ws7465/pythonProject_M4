def divide(first, second) :  #
    if second == 0 :  #
        from math import inf  #
        return inf #
    else :  #
        return first / second  #
# Примечания:
#
#     После импорта from math import inf возврат будет выглядеть так: return inf.
#     Деление в задаче обычное - '/'.
#     Не забудьте при импорте функций divide из разных модулей переопределить их
#     названия.