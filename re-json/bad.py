import requests
import json

my_req = requests.get(' https://www.breakingbadapi.com/api/deaths')

data = json.loads(my_req.text)
print(data)
max_death = 0
for elem in data:
    if elem['number_of_deaths'] > max_death:
        max_death = elem['number_of_deaths']
for elem in data:#можно убрать эту и след строку, тогда код будет перезаписывать новое максимальное значение смертей
    if elem['number_of_deaths'] == max_death:
        with open('max_death.json', 'w') as file:
            json.dump(elem, file, indent=4)
with open('max_death.json', 'r') as file:
    data = json.load(file)
    for elem in data:
        print(elem, ':', data[elem])
