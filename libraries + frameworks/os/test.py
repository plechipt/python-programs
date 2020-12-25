import os

os.chdir(r'C:\Users\plech\Desktop\Seberozvoj\Audioknihy + eknihy')
folders = ['kniha', 'zapisky']
book_name = input('Enter a book name: ')

for folder in folders:
    os.makedirs(f'{book_name}\{folder}')

os.chdir(r'C:\Users\plech\Desktop\Seberozvoj\Audioknihy + eknihy\%s\%s' % (book_name, folders[1]))

for i in range(1, 16):
    with open(f'{i} - .txt', 'w'):
        pass
