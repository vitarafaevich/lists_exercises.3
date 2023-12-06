num_1 = input("Введите целые числа через пробел: ")
list_1 = num_1.split()
num_2 = input("Введите целые числа через пробел: ")
list_2 = num_2.split()
number_1, number_2 = int(input()), int(input())
new = list_1[1:number_1 - 2]
print(new)