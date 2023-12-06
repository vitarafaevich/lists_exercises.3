sent = input("Введите предложение ")
sent_list = sent.split()
for i in range(len(sent_list)):
    sent_list[i] = sent_list[i].strip(",.!?")

print(sent_list)