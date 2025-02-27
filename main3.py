from fake_persian_name import fake_name as fpn
import os
from datetime import datetime
from functools import wraps


def logger(old_function):
    @wraps(old_function)

    def new_function(*args, **kwargs):
        start_time = datetime.now()
        result = old_function(*args, **kwargs)
        with open('main3.log', 'a') as file:
            stroka = f"Время: {start_time} Функция: {old_function} с аргументами {args} и {kwargs} Функция возвращает '{result}'\n"
            file.write(stroka)
        return result
    return new_function


def test_3():
    path = 'main3.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def pers_name_gen():
        name = fpn.generate_name("random")
        return  name

    pers_name_gen()

if __name__ == '__main__':
    test_3()