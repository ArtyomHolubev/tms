from datetime import datetime
import time


def time_function():
    time.sleep(1)
    print(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))


iteration = int(input('Введите количество выводов: '))
[time_function() for _ in range(iteration)]
