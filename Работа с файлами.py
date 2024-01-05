#
# Будет ошибка
# # 'C:\Users\User\Python\letters.py'
#
#  Ошибки не будет
#  r'C:\Users\User\Python\letters.py'
#
#  'C:\\Users\\User\\Python\\letters.py'
#
#  C:/Users/User/Python/letters.py'
#
#
# os.getcwd()
#
# os.listdir()
#
# my_cwd = os.getcwd()
# result = os.walk(my_cwd)
# for i, j, k in result:
#     for file in k:
#         print(file)
import os
print(os.path.isdir('C:\\Users\\User\\Python\Data\Samples'))

# Неверный способ
my_cwd = os.getcwd()
file_name = 'my_solution.py'
path = my_cwd + '\\' + file_name
# Метод мовитон


# Правильный
my_cwd = os.getcwd()
file_name = 'my_solution.py'
path = os.path.join(my_cwd, file_name)
print(path)

# os.mkdir() Создаёт папку
# os.makedirs() # mkdir -p dir1/dir2
# Пример использования

import os
new_dir = 'NewProject'
parent_dir = f'C:\\'
path = os.path.join(parent_dir, new_dir)
os.mkdir(path)  # Передаём путь
print(f'Директория {new_dir} создана: {os.listdir()}')
