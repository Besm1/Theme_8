def personal_sum(numbers):
    incorrect_numbers = 0
    result = 0
    for n in numbers:
        try:
            result += n
        except TypeError:
            incorrect_numbers += 1
            print(f'Некорректный тип данных для подсчёта суммы - {n}')
    # print(f'Вход:  {numbers}, сумма {result}, кол-во неправильных {incorrect_numbers}')
    return result, incorrect_numbers

def calculate_average(numbers):
    try:
        r, inc = personal_sum(numbers)
        return r / (len(numbers) - inc)
    except TypeError:
        print('В numbers записан некорректный тип данных.')
    except ZeroDivisionError:
        return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

