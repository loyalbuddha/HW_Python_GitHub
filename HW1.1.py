# 1. Поработайте с переменными, создайте несколько,
# выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

# 1. Поработайте с переменными, создайте несколько,
dummy_int = 30
dummy_str = 'ололо, я водитель нло'
dummy_b = True
dummy_fl = 1.1

# выведите на экран,
print('dummy_int =', dummy_int)
print('dummy_str =', dummy_str)
print('dummy_b =', dummy_b)
print('dummy_fl =', dummy_fl)

# запросите у пользователя несколько чисел и строк и сохраните в переменные,
dummy_int = int(input('введите целое число:'))
dummy_str = str(input('введите текст:'))
dummy_b = bool(input('введите булевское значение:'))
dummy_fl = float(input('введите значение с плавающей точкой:'))

# выведите на экран.
print('dummy_int =', dummy_int, ', type:', type(dummy_int))
print('dummy_str =', dummy_str, ', type:', type(dummy_str))
print('dummy_b =', dummy_b, ', type:', type(dummy_b))
print('dummy_fl =', dummy_fl, ', type:', type(dummy_fl))
