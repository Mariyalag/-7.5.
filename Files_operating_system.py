# import os
#
# print('Текущая директория:', os.getcwd())
# if os.path.exists('second'):
#     os.chdir('second')
# else:
#     os.mkdir('second')
#     os.chdir('second')
# print('Текущая директория:', os.getcwd())
# # os.makedirs(r'third\fourth')
#
# # for i in os.walk('.'):
# #     print(i)
# os.chdir(r'D:\PythonProject\pythonProjectPEREM\Modul 7')
# print('Текущая директория:', os.getcwd())
# # print(os.listdir())
# file = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isdir(d)]
# # print(dirs)
# # print(file)
# # os.startfile(file[3])
# # print(os.stat(file[3]).st_size)
# # os.system('pip install random2')


import os
import time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')