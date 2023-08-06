# Задание №8

# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

hike = ({'Иван': ('палатка', 'консервы', 'спички', 'вода'),
         'Артем': ('спальники', 'вода', 'нож', 'хлеб'),
         'Семен': ('крупа', 'посуда', 'хлеб')})

things = []
for key in  hike:
    for thing in  hike[key]:
        things.append(thing)
print('Все друзья взяли следующие вещи:', set(things))

     
my_thing = hike.keys()

my_set = set()
for friend in my_thing:
    my_set = set(hike[friend])

    for other_friends in [i for i in my_thing if i != friend]:
        my_set = my_set - set(hike[other_friends])
    if my_set:
        print(f'Вещи, которые взял только {friend} - {my_set}')

for friend in my_thing:
    to_remove = set(hike[friend])
    my_set = set()
    for other_friends in [i for i in my_thing if i != friend]:
        if not my_set:
            my_set = set(hike[other_friends])
        else:
           my_set = my_set & set(hike[other_friends])

    my_set -= to_remove

    if my_set:
        print(f'{friend} не взял {my_set}')