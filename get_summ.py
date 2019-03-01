def get_summ(num_one, num_two) :
    print('Сумма чисел:',(num_one+num_two))
   

try:
    num_one = int(input('Введите первое число - '))
    num_two = int(input('Введите второе число - '))
    get_summ(num_one, num_two)
except (ValueError) :
    print ('Вводите данные целыми цифрами!')