import random

class Buddist:
    def __init__(self, karma=0):
        self.__karma = karma

    def get_karma(self):
        return self.__karma

    def set_karma(self, sum_karma):
        self.__karma += sum_karma


def one_day(count):
    if random.randint(1, 10) == 5:
        with open('karma.log', 'a', encoding='utf-8') as file:
            exception = random.choice(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError'])
            file.write(f'в день {count}-й произошло это: {exception}\n')
            return False

    else:
        return random.randint(1, 7)



budda = Buddist()
day = 0
while budda.get_karma() < 500:
    day += 1
    if one_day(day):
        pass#continue
    else:
        budda.set_karma(one_day(day))

print('достиг нирваны')

