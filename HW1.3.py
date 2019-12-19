#3. Узнайте у пользователя число n.
#Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3.
#Считаем 3 + 33 + 333 = 369.

num_int = int(input('введите число:'))
print(int(str(num_int))+int(str(num_int)+str(num_int))+int(str(num_int)+str(num_int)+str(num_int)))