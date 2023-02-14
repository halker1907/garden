import random


garden = []

order = (
    ("ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис"),
    ("роза", "роза", "роза", "роза", "роза", "роза", "роза", "роза", "роза", "роза"),
    ("пион", "пион", "пион", "пион", "пион", "пион", "пион", "пион", "пион", "пион",)
)

for package in order:
    for seed in package:
        garden.append(seed)

weeds = ("борщевик", "крапива", "лопух")

for weed in weeds:
  for i in range(random.randint(5, 10)):
    garden.append(weed)

random.shuffle(garden)

print("сад до прополки:", garden)
print("")
print("идентификатор сада до прополки:", id(garden))

for weed in weeds:
    while weed in garden:
        garden.remove(weed)

print("---------------------------------------------------------------------------------")
print("сад после прополки:", garden)
print("")
print("идентификатор сада после прополки:", id(garden))

result = 0

for order in garden:
    if order == order:
        result += 1

print("")
print("В этом саду всего", result ,"растений!")