food = input("Сколько потрачено на еду: ")
transport = input("Сколько потрачено на транспорт: ")
recreation = input("Сколько потрачено на развлечения: ")
vsego = float(food) + float(transport) + float(recreation)
srednee = vsego / 3
print(f"Всего потрачено: {vsego:.2f}")
print(f"Средние расходы: {srednee:.2f}")