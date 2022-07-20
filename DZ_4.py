n = int(input('Кількість покупок '))
pokupku = []
for i in range(n):
    name = input('Введіть назву покупки')
    pokupku.append(name)
    # додати до списку pokupku елемент name

print('Всі покупки: ')
print(pokupku)