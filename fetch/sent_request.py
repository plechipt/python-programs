import requests

url = 'https://motion-detector.vercel.app/send-notification'


data = {
    'fcm_token': "d-knJbOyRn-VrNLUjqBglF:APA91bHveMhPOuM1lRcuaZk3yeiwKyGT9tO2x67SlgoE66y4gwfQs0y40ARwepELnY46GydK0yJ4MShjpa-gW5yYdBZVpiaimpgfWzw3NjStlkek5oHLkkobOJ4YvvBoK4mVmlAJqUo6"
}

r  = requests.post(url, json=data)
print(r.status_code)