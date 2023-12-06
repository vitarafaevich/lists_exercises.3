num = input("Введите целые числа через пробел: ")
num_list = num.split()

if '3' in num_list:
    num_list.remove('3')
    print(num_list)
else:
    print("Число 3 не было введено, пожалуйста, повторите попытку")