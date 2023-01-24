import os

strings = 0
fileslist = []
for _, _, files in os.walk('/Users/mymacbook/PycharmProjects/Python Basic26/Module26/'):
    for filename in files:
        if filename.endswith('.py'):
            fileslist.append(filename)
            print(filename)
print('\n')
for file in fileslist:
    with open(file) as f:
        ss = f.read().split('\n')
        for s in ss:
            if s.strip() and not s.startswith('#') and not s.startswith('"') and not s.startswith("'"):
                strings += 1

print('Всего строк:', strings)
