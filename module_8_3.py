from tkinter import mainloop
from tkinter.font import names


class IncorrectVinNumber(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Car:

    def __init__(self, model:str, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers


    def __is_valid_vin(self, vin):
        try:
            res = (1000000 <= vin <= 9999999)
        except TypeError:
            raise IncorrectVinNumber('Некорректный тип номера vin.')
        if not res:
            raise IncorrectVinNumber('Неверный диапазон номер vin.')
        return res

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return True
            else:
                raise IncorrectCarNumbers('Неверная длина номера')
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')


if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')

    try:
        third = Car('Model3', '2020202', 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 100500)
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')
