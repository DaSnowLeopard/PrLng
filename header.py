def data_input(): # заполнение списка с клавиатуры
    list = []
    size = int(input('input number of elements: '))
    for i in range(size):
        list.append(int(input('input element: ')))
    return list

def average_positive(list): # нахождение среднего арифметического положительеых чисел
    sum = 0
    for i in range(len(list)):
        if list[i] > 0:
            sum += list[i]
        else:
            sum = sum
    return sum

def negative_cnt(list): # количество отрицательных элементов
    cnt = 0
    for i in range(len(list)):
        if list[i] < 0:
            cnt += 1
        else:
            cnt = cnt
    return cnt

def negative_product(list): # произведение отрицательрных элементов
    product = 1
    for i in range(len(list)):
        if list[i] < 0:
            product *= list[i]
        else:
            product = product
    return product