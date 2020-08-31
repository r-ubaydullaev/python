profit = int(input("Введите выручку фирмы: "))
outlay = int(input("Введите расходы: "))
if profit >> outlay:
    profitability = profit - outlay
    rent = profitability / profit
    print(f"отличная работа.  У тебя есть {profitability} Рентабельность выручки")
    worker = int(input("Сколько людей работает: "))
    print(f"{profitability / worker} для одного работника")
elif profit == outlay:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")