#2. Пользователь вводит время в секундах.
#Переведите время в часы,
#минуты
#и секунды
#и выведите в формате чч:мм:сс.
#Используйте форматирование строк.

#2. Пользователь вводит время в секундах.
time_sec_int = int(input('введите время в секундах:'))

#Переведите время в часы,
time_h_int = time_sec_int // 3600

#минуты
time_m_int = (time_sec_int % 3600) // 60
# или так : time_m_int = (time_sec_int - time_h_int * 3600) // 60

#и секунды
time_s_int = time_sec_int - (time_h_int * 3600 + time_m_int * 60)

#для дебага:
#print(type(time_h_int))
#print(type(time_m_int))
#print(type(time_s_int))
#print(type(time_sec_int))
#print(time_h_int)
#print(time_m_int)
#print(time_s_int)
#print(time_sec_int)

#и выведите в формате чч:мм:сс.
#Используйте форматирование строк.
print('чч:мм:сс =',str(time_h_int)+':'+str(time_m_int)+':'+str(time_s_int))
