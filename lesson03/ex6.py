# case6:
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func():
    text = input("Please, input words here: ")
    print(text.title())
    return


int_func()


def int_func(n_words):
    separate_word = n_words.split(' ')
    total = []
    for i in separate_word:
        qty = str(i)
        first_letter = qty[:1].upper()
        word = first_letter + qty[1:]
        total.append(word)
    return total


print(int_func("testing ex six"))

