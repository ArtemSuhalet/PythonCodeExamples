def i_table(x):
    return x[1][0]

table = {}
number_rows = int(input('колво строк протокола: '))

for time in range(number_rows):
    ball, name = input('введите результат - имя через пробел: ').split()
    ball = int(ball)
    if name in table:
       if ball > table[name][0]:
           table[name][0] = ball
           table[name][1] = time
    else:
        table[name] = [ball, time]
table = list(table.items())#sort  работает ток со списками
print(table)
table.sort(key = i_table, reverse = True)# True - сорт по убыванию, false -  по возраст.
print(table)
print('\nитоги соревнований: ')
for i in 0, 1, 2:
    print(i + 1, 'место', table[i][0], table[i][1][0])