site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, depth):
    if key in struct:
        return struct[key]
    if depth > 1:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key, depth - 1)
                if result:
                    break
        else:
            result = None

        return result

def count(site):
    return max(count(v) if isinstance(v, dict) else 0 for v in site.values()) + 1
print(count(site))

user_key = input('введите ключ: ')
a = input('Хотите ввести максимальную глубину? Y/N:').lower()
if a == 'y':
    depth_search = int(input('Введите глубину поиска: '))
    value = find_key(site, user_key, depth_search)
else:
    value = find_key(site, user_key, count(site))
if value:
    print(value)
else:
    print('ключ не найден')

