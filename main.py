import random

english_list = ["dog", "god", "wod"]
list_coding = {"d":"--.", "o":"..-", "w":"---","g":"..."}
answers = []

def get_word():
    return random.sample(english_list, 1)[0]

def morse_encode(world):
    encode_list = []
    for word in world:
        if word in list_coding:
            encode_list.append(list_coding[word])
        if word == "d":
            encode_list.append("--..-")
        elif word == "o":
            encode_list.append("-.-")
        elif word == "w":
            encode_list.append("..--..")
        elif word == "g":
            encode_list.append("----")
    return encode_list




def print_statics(list):
    count_plus = 0
    count_munis = 0
    for answer in list:
        if answer == "True":
            count_plus += 1
        else:
            count_munis += 1
    print(f"Всего задачек: {len(list)} \n"
          f"Отвечено верно: {count_plus} \n"
          f"Отвечено не верно: {count_munis}")

input("Сегодня мы потренируем морзянку, для старта нажмите Enter")
count_pop = len(english_list)

while count_pop > 0:
    word = get_word()
    print(f"Слово {morse_encode(word)}")
    aswer_user = input("Введите ответ: ")
    if aswer_user == word:
        answers.append("True")
        print("Правильно, молодец!")
    else:
        print(f"Неверно, это слово {word}")
        answers.append("False")
    count_pop -= 1
print()
print_statics(answers)
