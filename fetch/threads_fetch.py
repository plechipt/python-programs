import requests
import threading

url = 'https://open-ai-dalle-2-image-generator-api-rezaan6.vercel.app/api/v1/dalle'

data = {
    'prompt': 'test'
}

def do_request():
    while True:
        response = requests.post(url, json=data).text
        print(response)

threads = []

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()