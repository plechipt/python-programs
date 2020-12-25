import os

os.chdir(r"C:\Users\Admin\Desktop\Drive\seberozvoj\Audioknihy + eknihy")
folders = ['kniha', 'zapisky']
book_name = input('\nEnter the book name: ')

for folder in folders:
    os.makedirs(f'{book_name}/{folder}')

os.chdir(r"C:\Users\Admin\Desktop\Drive\seberozvoj\Audioknihy + eknihy\%s\%s" % (book_name, folders[1]))

for i in range(1, 21):
    with open(f'{i} - .txt', 'w') as f:
        pass
