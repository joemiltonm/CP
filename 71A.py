

number_of_words = int(input())
word_list = []

for i in range(number_of_words):
    word = input()
    word_list.append(word)

for i in word_list:
    if len(i) > 10:
        print(i[0]+str(len(i)-2)+i[-1])
    else:
        print(i)
