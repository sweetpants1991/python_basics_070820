# case05:
# Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделенных пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    try:
        with open('file.txt', 'w+') as file_obj:
            line = input('Enter number (use spaces): \n')
            file_obj.writelines(line)
            numbers = line.split()

            print(sum(map(int, numbers)))
    except IOError:
        print('File Error')
    except ValueError:
        print('Wrong number!')


summary()
