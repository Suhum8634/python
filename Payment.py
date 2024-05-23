# здесь код для высчитывания зарплаты за день
# hour = float(input("Введите, сколько часов вы отработали: "))
days = 0
sum = 0
num = 0
while days < 5:
    hour = int(input("Введите, сколько часов вы отработали: "))
    if hour < 6:
        num = hour * 5
        sum += num
        days += 1
    if hour >= 6:
        num = (hour - 6) * 5 + 24
        sum += num
        days += 1
print(sum)
