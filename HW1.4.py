#4. Пользователь вводит целое положительное число.
#Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.

num_int = int(input('введите целое положительное число:'))

#узнаём порядок числа
m = 1
i = 1
while i != 0:
    i = num_int // 10**m
    m=m+1
num_len_int = m-1
#for debug print('число имеет',num_len_int,'знаков')

#перебираем цифры числа и выясняем наибольшую цифру
num_dummy = 0
i = 1
m = 1
num_dummy_2 = 0
#будем разбивать число на части слева направо
#и сравнивать текущую цифру с предудущей.
#Если текущая цифра больше предыдущей, то мы будем записывать её в максимум
num_max = num_int // 10**(num_len_int-1)
print(num_max)
while i <= num_len_int:
    num_dummy = num_int//(10**(i-1)) - ( num_int // (10**i) )*10
    while num_dummy <= num_dummy_2 and num_dummy >= num_max:
        num_max = num_dummy_2
        # for debug print('i=',i,',num_dummy=',num_dummy,',num_max=',num_max)
        break
    num_dummy_2 = num_dummy
    i += 1
print('максимальная цифра из введённого числа:',num_max)