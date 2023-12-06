def sorted(st):
    ch_list = list(st)
    ch_list.sort()
    sorted = ''.join(ch_list)
    return sorted

st = input("Введите строку: ")
result = sorted(st)
print("Отсортированная строка:", result)