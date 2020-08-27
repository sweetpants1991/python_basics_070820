# case02:
# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file = open('text.txt', 'r')
content = file.read()
print(f'File content: \n {content}')
file = open('text.txt', 'r')
content = file.readlines()
print(f'Qty of strings - {len(content)}')
file = open('text.txt', 'r')
content = file.readlines()
for i in range(len(content)):
    print(f'Qty of symbols {i + 1} - of string {len(content[i])}')
file = open('text.txt', 'r')
content = file.read()
content = content.split()
print(f'Qty of words - {len(content)}')
file.close()