

time_in_sec = int(input("Введите время в секундах: "))
hours = time_in_sec // 3600 #часы ЧЧ:
residue = time_in_sec % 3600 #остатки
minutes = residue // 60  #минуты ММ:
sec = residue % 60 #секунды СС:
print(f"Время в формате чч:мм:сс: {hours} : {minutes} : {sec} ")