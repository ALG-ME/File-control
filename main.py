# Создание файла "sample.txt" и запись текста в него
with open('sample.txt', 'w', encoding='utf-8') as file:
    file.write('тырыпыры "sample.txt".\nещё что то тут.')

# Чтение содержимого файла и вывод на экран
with open('sample.txt', 'r', encoding='utf-8') as file:
    contents = file.read()
    print(contents)


# Запрос у пользователя строки текста
user_input = input(str('Введите строку текста: '))

# Запись введенной строки в файл "user_input.txt"
with open('user_input.txt', 'w', encoding='utf-8') as file:
    file.write(user_input)

print('Строка успешно записана в файл "user_input.txt".')


# Подсчет количества строк в файле "sample.txt"
with open('sample.txt', 'r', encoding='utf-8') as file:
    line_count = sum(1 for line in file)

print("Количество строк в файле 'sample.txt':", line_count)
