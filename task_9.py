'''
Программа получает на вход текст, который вводится с клавиатуры.
Признак окончания ввода текста - пустая строка.
Программа должна вывести слова, в порядке от наиболее часто встречающегося к менее встречающемуся.
Если слова встречаются в тексте одинаковое количество раз, то они должны выводиться в порядке их появления в тексте.
Программа выводит каждое слово в отдельной строке в нижнем регистре. Знаки препинания должны быть исключены
'''

def sort_words(text):
    word_list = text.lower().split()
    w_cnt = {}

    for word in word_list:
        word = word.strip(",.!?")
        if word in w_cnt:
            w_cnt[word] += 1
        else:
            w_cnt[word] = 1

    sorted_w = sorted(w_cnt.items(), key=lambda x: (-x[1], word_list.index(x[0])))

    for word, count in sorted_w:
        print(word)


text = ""
while True:
    line = input("Введите текст: ")
    if not line:
        break
    text += " " + line

sort_words(text)