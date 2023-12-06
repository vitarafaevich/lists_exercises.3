num = input("Введите целые числа через пробел: ")
num_list = num.split()
sum = 0
for num in num_list:
    sum += int(num)
    average = sum / len(num_list)
print(round(average))
