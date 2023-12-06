numbers = []
for i in range(10):
    num = int(input("Введите 10 целых чисел"))
    numbers.append(num)

new = []
for i in range(9):
    new.append(numbers[i] + numbers[i+1])

print(new)