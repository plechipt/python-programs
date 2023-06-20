import time
import serial
import requests

# Open the serial port
ser = serial.Serial('COM1', 9600)  # Replace 'COM3' with the appropriate port and baud rate

time.sleep(2)

while True:
    # Read data from the serial port
    data = ser.readline().decode().strip()

    if data == "alarm on":
        print("Motion detected! Executing actions...")

url = 'https://motion-detector.vercel.app/send-notification'


data = {
    'fcm_token': "e80Z8xofQSKL2v0xKMo2Nh:APA91bEg_s00A1gP9M2rdlRF0SODuQHgQ35_hF313prwunEXfkVNOd3eM1sD6mw-hb8G31fRb5titRI-f_Xpi_KJeJDlV5tTxKK1UO_q1RDAgp8fGxom0a8jU7a_giTzd-R3w0MBqMrf"
}

#r  = requests.post(url, json=data)
#print(r.status_code)