# Задача 5
prices = [12.23, 42, 9.99, 114.99, 55, 90, 1024, 12.34, 66.01, 89.07, 246.80, 13.57, 890, 88.88, 45.67]
print(prices)
print(id(prices))
for el in prices:
    if (el % 1) * 100 < 10:
        print(f'{int(el):0d} рублей 0{(el % 1) * 100:.0f} копеек; ', end='')
    else:
        print(f'{int(el):0d} рублей {(el % 1) * 100:.0f} копеек; ', end='')
print('*')
print(id(prices))
prices.sort()
print(prices)
print(id(prices))
prices_new = sorted(prices)
prices_new.reverse()
print(prices_new)
print(id(prices_new))
print(prices)
print(id(prices))
prices.sort()
print(prices[:5])
