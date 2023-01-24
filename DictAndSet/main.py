def height(person):
    if person not in p_tree:#если person в множестве не является child то он получает 0
        return 0
    else:
        return 1 + height(p_tree[person])# если person -  child, то + 1 к heights его предка


p_tree = {}
n = int(input('введите колво пар: '))
for i in range(n - 1):
    child, parent = input('введите пару(ребенок родитель): ').split()
    p_tree[child] = parent
print(p_tree)


heights = {}# высота ветки на дереве
for person in set(p_tree.keys()).union(set(p_tree.values())):#создаем множество чтобы исключить повторы имен
    heights[person] = height(person)#отправляем в функцию
print(heights)


for key, value in sorted(heights.items()):
    print(key, value)