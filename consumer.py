from DataProcessor import DataProcessor
import os
import sys

if __name__ == '__main__':
    cloudampq_url = os.environ.get('cloudampq_url')
    if cloudampq_url is None:
        print("Please set the cloudampq_url environment variable")
        sys.exit(1)

    dp = DataProcessor(cloudampq_url)
    user_answer = input("What queue do you want to consume? (1) IoT Equipo 16 (2) IoT Equipo 16.temperature (3) IoT Equipo 16.humidity (4) IoT Equipo 16.complex: ")
    if user_answer == '1':
        dp.consume('IoT Equipo 16')
    elif user_answer == '2':
        dp.consume('IoT Equipo 16.temperature')
    elif user_answer == '3':
        dp.consume('IoT Equipo 16.humidity')
    else:
        dp.consume('IoT Equipo 16.complex')



