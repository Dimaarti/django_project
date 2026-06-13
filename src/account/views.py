from functools import lru_cache



def positiv_sum(lst):
    if not lst:
        return 0

    count_sum = lst[0] if lst[0] > 0 else 0
    return count_sum + positiv_sum(lst[1:])


my_lst = [1, 2, 1, -5]

print(positiv_sum(tuple(my_lst)))
