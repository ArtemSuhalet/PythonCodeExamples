import re

def check(number):
    if re.fullmatch(r'[АВЕКМНОРСТУХabekmhopctyx]\d{3}[АВЕКМНОРСТУХabekmhopctyx]{2}\d{2,3}', number):
        return print('частник')
    if re.fullmatch(r'[АВЕКМНОРСТУХabekmhopctyx]{2}\d{5,6}', number):
        return print('такси')
    return print('UFO')


check(input('введите номер '))
# вариант -А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666