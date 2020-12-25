import os

os.chdir('/run/user/1000/gvfs/google-drive:host=gmail.com,user=loxtox74/1Su-J5OQU9z9jwJH89wKfrbRmZxnSe1Qf/1XNQBh1hzkdV2ZZVfBU9mfdnADbs093GG')
names = ['book', 'zapisky']

book_name = input('Enter a book name: ')

for name in names:
    os.makedirs(f'{book_name}/{name}')

os.chdir(f'/run/user/1000/gvfs/google-drive:host=gmail.com,user=loxtox74/1Su-J5OQU9z9jwJH89wKfrbRmZxnSe1Qf/1XNQBh1hzkdV2ZZVfBU9mfdnADbs093GG/{book_name}/{name}')
for i in range(1, 21):
    with open(f'{i} - .txt', 'w') as f:
        f.write('idk')
