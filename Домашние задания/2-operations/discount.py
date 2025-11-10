coust = input("Сколько стоит товар без скидки? ")
discount = input("Какой процент скидки? ")
itogo = float(coust) - (float(coust) * int(discount) / 100)
print(f"Цена товара со скидкой: {itogo:.2f}")