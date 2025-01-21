import header

numbers = header.data_input()
print('list:', numbers)

av_positive = header.average_positive(numbers)
print('arithmetic mean of positive elements:', av_positive)

cnt_negative = header.negative_cnt(numbers)
print('number of negative elements:', cnt_negative)

product_negative = header.negative_product(numbers)
print('product of negative elements:', product_negative)