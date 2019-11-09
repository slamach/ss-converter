# Перевод из одной СС в другую по заданному шаблону:
# исход_СС рез_СС число1 число2 число3 число4 число5
#
# Программа работает только с положительными исходными числами!
#
# Работа с нега-позиционными СС доступна только в формате:
# НП_СС -> 10-ная
#
# @ Свиридов Дмитрий, PЗ113

FILE_IN = "iofiles/input.txt"
FILE_OUT = "iofiles/output.txt"

ALPHABET = "0123456789ABCDEF"  # до 16-ричной


def datain():
    """ Сбор данных с файла """
    data = []
    with open(FILE_IN, 'rt') as fin:
        for line in fin:
            data.append(tuple(line.strip().split()))
    return data


def dataout(data):
    """ Запись данных в файл """
    with open(FILE_OUT, 'wt') as fout:
        for line in data:
            print(line, file=fout)


def convert_to_dec(num, key):
    """ Перевод числа из X-ричной СС в десятичную """
    res = 0
    for ind, n in enumerate(num):
        res += ALPHABET.index(n) * key**(len(num) - (ind+1))
    return res


def convert_from_dec(num, key):
    """ Перевод числа из десятичной СС в X-ричную """
    res = ""
    while num // key:
        res = ALPHABET[num % key] + res
        num //= key
    return ALPHABET[num % key] + res


def main():
    data = datain()
    res_data = []  # тут будет храниться итоговый массив строк ответа

    for line in data:
        start_key, end_key = int(line[0]), int(line[1])
        res_nums = [] # тут будут храниться переводы текущей строки

        for num in line[2:]:
            # Проверка на СС, с которыми программа не умеет работать
            if end_key < 0 or (start_key < 0 and end_key != 10):
                res_num = "-"
            # Проверка на лишнюю работу
            elif end_key == 10:
                res_num = convert_to_dec(num, start_key)
            elif start_key == 10:
                res_num = convert_from_dec(int(num), end_key)
            else:
                res_num = convert_from_dec(convert_to_dec(num, start_key), end_key)

            res_nums.append(f"{num} -> {res_num}")
        
        # Форматирование строки ответа
        res_data.append(f"{start_key} -> {end_key}: " + " | ".join(res_nums))
    
    dataout(res_data)


main()
