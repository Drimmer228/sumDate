import datetime

year = 0
while year == 0:
    try:
        print("Введите год для подсчета суммы")
        year = int(input())
        if(year<=0):
            year = 0
    except:
        print("Введен неверный год")

sum = 0
for i in range(13):
    for j in range(32):
        try:
            date = datetime.date(year, i, j)
            if(j>=10):
                firstNumber = int(date.day / 10)
                secondNumber = int(date.day % 10)
                sum += firstNumber + secondNumber
            else:
                sum += date.day
        except:
            j = 31
print("Сумма дней = ", sum)