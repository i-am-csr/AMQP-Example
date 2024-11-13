from Sensor import Sensor
import os
import sys

if __name__ == '__main__':
    cloudampq_url = os.environ.get('cloudampq_url')
    if cloudampq_url is None:
        print("Please set the cloudampq_url environment variable")
        sys.exit(1)

    sensor = Sensor(cloudampq_url)
    user_answer = input("What do you want to simulate? (1) Temperature (2) Humidity (3) Both: ")
    if user_answer == '1':
        temperature = input("Enter the temperature: ")
        answer = sensor.send_message('IoT Equipo 16.temperature', f'{{"temperature": {temperature}}}')
        print(answer)
    elif user_answer == '2':
        humidity = input("Enter the humidity: ")
        answer = sensor.send_message('IoT Equipo 16.humidity', f'{{"humidity": {humidity}}}')
        print(answer)
    else:
        temperature = input("Enter the temperature: ")
        humidity = input("Enter the humidity: ")
        answer = sensor.send_message('IoT Equipo 16.complex', f'{{"temperature": {temperature}, "humidity": {humidity}}}')
        print(answer)
