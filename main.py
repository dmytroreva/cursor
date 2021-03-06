import inspect
import functools


def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]


int_a, str_b, set_c, lst_d, dict_e = 55, 'cursor', {1, 2, 3}, [1, 2, 3], {'a': 1, 'b': 2, 'c': 3}
list_for_example = [int_a, str_b, set_c, lst_d, dict_e]

for first_example_variables in list_for_example:
    print(f'id of variable {retrieve_name(first_example_variables)[0].__repr__()} = {id(first_example_variables)}')

lst_d. extend([4,5])
print(f'id of lst_d = {id(locals())})')
for third_example_variables in list_for_example:
    print(f'tipe of variable {retrieve_name(third_example_variables)[0].__repr__()} = {type(third_example_variables)}')


print(
    f'is type of int_a = int - {isinstance(int_a, int)}'
    , f'is type of str_b = str - {isinstance(str_b, str)}'
    , f'is type of set_c = set - {isinstance(set_c, set)}'
    , f'is type of lst_d = lst - {isinstance(lst_d, list)}'
    , f'is type of dict_e = dict - {isinstance(dict_e, dict)}'
    , sep='\n'
)

apples_count = 3
peaches_count = 9
print('Anna has {} apples and {} peaches.'.format(apples_count, peaches_count))

print('Anna has {1} apples and {0} peaches.'.format(peaches_count, apples_count))

print('Anna has {apples} apples and {peaches} peaches.'.format(apples=apples_count, peaches=peaches_count))

print('Anna has {0:5} apples and {0:3} peaches.'.format(peaches_count, apples_count))

print(f'Anna has {apples_count} apples and {peaches_count} peaches.')

print('Anna has %s apples and %s peaches.' % (apples_count, peaches_count))

apples_peaches_dict = {'apples': apples_count, 'peaches': peaches_count}
print('Anna has %(apples)s apples and %(peaches)s peaches.' % apples_peaches_dict)

comprehension_list_from_regular = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(f'comprehension_list_from_regular = {comprehension_list_from_regular}')

regular_list_from_comprehension = []
for num in range(10):
    if num % 2 == 0:
        regular_list_from_comprehension.append(num // 2)
    else:
        regular_list_from_comprehension.append(num * 10)
print(f'regular_list_from_comprehension = {regular_list_from_comprehension}')

first_comprehension_dict_from_regular = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(f'first_comprehension_dict_from_regular = {first_comprehension_dict_from_regular}')

second_comprehension_dict_from_regular = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(f'second_comprehension_dict_from_regular = {second_comprehension_dict_from_regular}')

first_regular_dict_from_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        first_regular_dict_from_comprehension[x] = x ** 3
print(f'first_regular_dict_from_comprehension = {first_regular_dict_from_comprehension}')

first_regular_dict_from_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        first_regular_dict_from_comprehension[x] = x ** 3
print(f'first_regular_dict_from_comprehension = {first_regular_dict_from_comprehension}')

foo = lambda x, y: x if x < y else y
print(f'lambda function from def = {foo(2, 10)}')

def def_from_foo(x, y, z):
    if y < x > z:
        return z
    else:
        return y


print(f'def from lambda function = {def_from_foo(4, 7, 5)}')

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort.sort()
print(f'sorted list from min to max = {lst_to_sort}')

lst_to_sort.sort(reverse=True)
print(f'sorted list from max to min = {lst_to_sort}')
lst_to_sort = list(map(lambda x: x * 2, lst_to_sort))
print(f'updated list by multiplied each element by 2 = {lst_to_sort}')

list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_C = list(map(lambda x, y: x * y, list_A, list_B))
print(f'raised each list number by corresponding Number on another list = {list_C}')

sum_of_lst_to_sort_values = functools.reduce(lambda x, y: x + y, lst_to_sort)
print(f'sum of all lst_to_sort values = {sum_of_lst_to_sort_values}')

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort_with_only_odd_numbers = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(f'only odd numbers in lst_to_sort = {lst_to_sort_with_only_odd_numbers}')

list_of_only_negative_numbers = list(filter(lambda x: x < 0, range(-10, 10)))
print(f'only negative numbers in range(-10, 10) = {list_of_only_negative_numbers}')

list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
list_of_common_values = list(filter(lambda x: x in list_1, list_2))
print(f'the values that are common to the two lists = {list_of_common_values}')






