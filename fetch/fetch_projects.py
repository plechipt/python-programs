import requests

urls = [
    'https://my-todo-app-frontend-site.netlify.app', 'https://ecommerce-app-frontend.netlify.app',
    'https://elibrary-app-frontend.netlify.app',  
] 

for url in urls:
    x = requests.get(url)
    print(x.status_code)