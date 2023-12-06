num = input("Введите целые числа через пробел: ")
num_list = num.split()
cnt_1 = 0
cnt_2 = 0
for i in num_list:
    if int(i) % 2 != 0:
        cnt_1 += int(i)
    else:
        cnt_2 += int(i)
print('Сумма четных', cnt_2)
print('Сумма нечетных', cnt_1)