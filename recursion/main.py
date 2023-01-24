def hanoi(n, start, finish):
    if n <= 0:
        return
    temp = 6 - start - finish
    hanoi(n - 1, start, temp)#перенести диск с start стержня на temp
    print('перенести диск', n, 'со стержня', start, 'на стержень', finish)
    hanoi(n - 1, temp, finish)#перенести диск с temp стержня на finish



hanoi(int(input('колво колец: ')), 1, 3)# 1 -start, 3 - finish, temp - средний стержень