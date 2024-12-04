from math import log, sqrt
# # # # # a = int(input())

# # # # # b = 2*a
# # # # # c = 3*a
# # # # # d = 4*a
# # # # # e = 5*a

# # # # # print(a, b, c, d, e, sep="---")

# # # # # a = 82 // 3**2 % 7
# # # # # print(a)

# # # # # naselenie=int(input())//-2*-1
# # # # # ostatok = naselenie%2
# # # # # ob= naselenie+ostatok
# # # # # print(naselenie)
# # # # # sm = int(input())//100
# # # # # # bn = sm//100
# # # # # print(sm)

# # # # input_minutes = int(input())
# # # # h = input_minutes//60
# # # # m = input_minutes%60
# # # # print (input_minutes, "мин - это", h, "час", m, 'минут.')


# # # mesto = int(input())
# # # a = 36-mesto
# # # b = a//4
# # # print(9-b)

# # num = int(input())
# # last_digit = num % 10
# # first_digit = num // 10

# # print('Число десятков =', first_digit)
# # print('Число единиц =', last_digit)

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10

# print('Сумма цифр =', last_digit + first_digit)

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10

# print('Искомое число =', last_digit * 10 + first_digit)

# num = int(input())
# a = num // 1000
# b = (num % 10**3) // 10**2
# c = (num % 10**2) // 10
# d = num % 10
# print ("Цифра в позиции тысяч равна", a)
# print ("Цифра в позиции сотен равна", b)
# print ("Цифра в позиции десятков равна", c)
# print ("Цифра в позиции единиц равна", d)
# s = 13
# k = -5
# d = s + 2
# s = d
# k = 2 * s
# print(s + k + d)

# a = 17 // (23 % 7)
# b = 34 % a * 5 - 29 % 4 * 3
# # print(a * b)

# print("*****************")
# print("*               *")
# print("*               *")
# print("*****************")

# a = int(input())
# b = (a*123)
# # c = (100*a+10*a+a)
# print (b)

# Программа, которая определяет, является число четным или нечетным
# a = int(input())
# count = 0
# if a % 2 == 0:
#     count = count+1
#     print (count)
# else:
#     print ("НЕчетное")

# что такое делимое, делитель, частное
# остаток от деления при делении положительных и отрицательных чисел
# что есть как бы шкала чисел ... - 3, -2, -1, 0, 1, 2, 3, ... в которой увеличение идёт слева==> направо, т.е. 3 > 2, но -3 < -2 и в какую сторону округлять принято в python, когда находим остаток от деления отрицательных чисел
# разобраться с теорией и посмотреть комментарии, в них довольно много полезных примеров.

# Программа, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: 
# сумма первой и последней цифр равна разности второй и третьей цифр
# num = int(input())
# a = num // 1000
# b = (num % 10**3) // 10**2
# c = (num % 10**2) // 10
# d = num % 10
# summ_a = a + d
# summ_b = b - c
# if summ_a == summ_b:
#     print ("ДА")
# else:
#     print ("НЕТ")

# Программа, которая определяет, разрешён ли пользователю доступ к интернет-ресурсу или нет
# num = int(input())
# if num < 18:
#     print ("Доступ запрещен")
# if num >= 18:
#     print ("Доступ разрешен")

# Программа, которая определяет, являются ли три заданных числа (в указанном порядке) 
# последовательными членами арифметической прогрессии.
# num_a = int(input())
# num_b = int(input())
# num_c = int(input())
# # prog = (num_b-num_a)+num_b
# if num_b - num_a == num_c - num_b:
#     print ("YES")
# else:
#     print ("NO")

# Программа, которая определяет наименьшее из двух чисел
# num_a = int(input())
# num_b = int(input())
# if num_a > num_b:
#     print (num_b)
# else:
#     print(num_a)

# Программа, которая определяет наименьшее из четырёх чисел
# num_a = int(input())
# num_b = int(input())
# num_c = int(input())
# num_d = int(input())
# if num_a <= num_b:
#     ab = num_a
# else:
#     ab = num_b
# if num_c <= num_d:
#     cd = num_c
# else:
#     cd = num_d
# if ab < cd:
#     print (ab)
# else:
#     print(cd)

# # Программа, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится
# age = int(input())
# if age <= 13:
#     print ("детство")
# if 14 <= age <= 24:
#     print ("молодость") 
# if 25 <= age <= 59:
#     print("зрелость")
# if age >= 60:
#     print("старость")

# Программа, которая считывает три числа и подсчитывает сумму только положительных чисел
# num_a = int(input())
# num_b = int(input())
# num_c = int(input())
# if num_a >= 0:
#     aa = num_a
# else:
#     aa = 0
# if num_b >= 0:
#     bb = num_b
# else:
#     bb = 0
# if num_c >= 0:
#     cc = num_c
# else:
#     cc = 0
# summa = aa+bb+cc
# if summa > 0:
#     print(summa)
# else:
#     print(0)
    
# a, b, c = int(input()), int(input()), int(input())
# if a < 0:
#     a = 0
# if b < 0:
#     b = 0
# if c < 0:
#     c = 0
# d = a + b + c
# print(d)

# num1 = 34
# num2 = 81
# if num1 // 9 == 0 or num2 % 9 == 0:
#     print('число', num1, 'выиграло')
# else:
#     print('число', num2, 'выиграло')

# a = 7

# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5

# p = (a + b) * (a + b)
# print(p)

# Программа, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам
# x = int(input())
# if (-30 < x <= -2) or (7 < x <= 25):
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

# Программа, определяющую, является ли введённое число красивым
# x = int(input())
# if (999 < x <= 9999) and (x%7==0 or x%17==0): #(x // 1000 % 10 == 0) and (x//7 or x//17):
#     print("YES")
# else:
#     print("NO")

# Программа, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами
# a = int(input())
# b = int(input())
# c = int(input())
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("YES")
# else:
#     print("NO")

# Программа, которая определяет, является ли год с данным номером високосным. 
# date = int(input())
# if (date % 4 == 0 and date%100 !=0) or (date%400 == 0):
#     print("YES")
# else:
#     print("NO") 

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1==x2 or y1==y2:
#     print ("YES")
# else:
#     print ("NO")

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if -1 <= (x2-x1) <=1 and -1 <= (y2-y1) <=1:
#     print ("YES")
# else:
#     print ("NO")

# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print("Равносторонний")
# elif a == b and c != a and c!= b:
#     print("Равнобедренный")
# elif a == c and b != a and b != c:
#     print("Равнобедренный")
# elif b == c and a != b and a != c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# a = int(input())
# b = int(input())
# c = int(input())
# if a < b < c or a > b > c:
#     print (b)
# elif b < a < c or b > a > c:
#     print(a)
# else:
#     print (c)

# a = int(input())
# a1 = 31
# b1 = 30
# c1 = 28

# if a in (1, 3, 5, 7, 8, 10, 12):
#     print (a1)

# # if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
#     # print (a1)
# elif a == 2:
#     print (c1)
# else:
#     print(b1)

# a = int(input())
# if a < 60:
#     print("Легкий вес")
# elif 60 <= a <= 63:
#     print("Первый полусредний вес")
# elif 64 <= a < 69:
#     print("Полусредний вес")

# a = int(input())
# b = int(input())
# c = input()
# if c == "+":
#     sl = a + b
#     print (sl)
# elif c == "-":
#     mi = a - b
#     print (mi)
# elif c == "*":
#     um = a*b
#     print(um)
# elif b!=0 and c == "/":
#     delenie = a/b
#     print (delenie)
# elif b == 0 and c == "/":
#     print ("На ноль делить нельзя!")    
# else:
#     print ("Неверная операция")

# a = input()
# b = input()
# red = "красный"
# blue = "синий"
# yellow = "желтый"
# if a == red and b == blue or a == blue and b == red:
#     print("фиолетовый")
# elif a == blue and b == yellow or a == yellow and b == blue:
#     print("зеленый")
# elif a == red and b == yellow or a == yellow and b == red:
#     print ("оранжевый")
# elif a == b and (a == red or a == blue or a == yellow):
#     print (a)
# else:
#     print("ошибка цвета")

# num = int(input())
# if num == 0:
#     print("зеленый")
# elif num % 2==0 and 0 < num <= 10 or 19 < num <= 28:
#     print ("черный") 

# elif num % 2==0 and 11 <= num <= 18 or 29 <= num <= 36:
#     print("красный")

# # нечетные с (1 по 10) и с (19 по 28) =>
# elif num % 2 != 0 and 0 < num <= 10 or 19 <= num <= 28:
#     print("красный")

# # нечетные с (11 по 18) и с (29 по 36) => красный
# elif num % 2 != 0 and 11 <= num <= 18 or 29 <= num <= 36:
#     print("красный")

# if num < 0 or num > 36:
#     print("ошибка ввода")

# num = int(input())
# if num == 0:
#     print("зеленый")

# elif num % 2 != 0 and 0 < num <= 10:
#     print("красный")
# elif num % 2 == 0 and 0 < num <= 10:
#     print("черный")
# elif num % 2 != 0 and 11 <= num <= 18: 
#     print("черный")
# elif num % 2==0 and 11 <= num <= 18:
#     print("красный")
# elif num % 2 != 0 and 19 <= num <= 28:
#     print("красный")
# elif num % 2==0 and 19 < num <= 28:
#     print ("черный") 
# elif num % 2 != 0 and 29 <= num <= 36:
#     print("черный")
# elif num % 2 == 0 and 29 <= num <= 36:
#     print("красный")
# elif num < 0 or num > 36:
#     print("ошибка ввода")




# elif num % 2==0 and 0 < num <= 10 or 19 < num <= 28:
#     print ("черный") 

# elif num % 2==0 and 11 <= num <= 18 or 29 <= num <= 36:
#     print("красный")

# # нечетные с (1 по 10) и с (19 по 28) =>
# elif num % 2 != 0 and 0 < num <= 10 or 19 <= num <= 28:
#     print("красный")

# # нечетные с (11 по 18) и с (29 по 36) => красный
# elif num % 2 != 0 and 11 <= num <= 18 or 29 <= num <= 36:
#     print("красный")

# if num < 0 or num > 36:
#     print("ошибка ввода")


# a = int(input())
# count = 0
# if a % 2 == 0:
#     count = count+1

# s, v1, v2 = float(input()), float(input()), float(input())
# # v1 = v1/60
# # v2 = v2/60
# t = s/(v1+v2)
# print(t)

# a = float(input())
# if a != 0:
#     b = 1/a
#     print(b)
# elif a==0:
#     print ("Обратного числа не существует")
    
# a = float(input())
# tc = 5/9*(a-32)
# print(tc)

# a = float(input())
# if a <=1:
#     h = 10.5*a 
#     print(h)
# elif  1 < a <=2:
#     h = 10.5*a
#     print(int(h)) 
# elif a>2:
#     h = (10.5*2)+((a-2)*4)
#     print (int(h))

# a = float(input())
# b = int(a)
# c = a - b
# print (c)

# num = max(1, 3, -5, 7) + min(-3, 6, -8, -1) + abs(-17)
# print(num)

# a, b, c = int(input()), int(input()), int(input())
# max1= max(a, b, c)
# min1 = min(a, b, c)
# crednee = (a+b+c) - max1 - min1
# print (max1)
# print (crednee)
# print (min1)


# num = int(input())
# a = num // 100 % 10
# b = num //10 % 10
# c = num // 1 % 10
# max1 = max(a, b, c)
# min1 = min(a, b, c)
# crednee = (a+b+c) - max1 - min1
# raznost = max1 - min1
# if raznost == crednee:
#     print("Число интересное")
# else:
#     print("Число неинтересное")

# num1 = float(input())
# num2 = float(input())
# num3 = float(input())
# num4 = float(input())
# num5 = float(input())
# x = abs(num1) + abs(num2) + abs(num3) + abs(num4) + abs(num5)
# print(x)

# p1 = float(input())
# p2 = float(input())
# q1 = float(input())
# q2 = float(input())
# x = abs(p1 - q1) + abs (p2-q2)
# print (int(x))

# str1 = '1'
# str2 = str1 + '2' + str1
# str3 = str2 + '3' + str2
# str4 = str3 + '4' + str3
# print(str4)

# name = input()
# len1 = len(name)
# print (f"Футбольная команда {name} имеет длину {len1} символов")

# city1, city2, city3  = input(), input(), input()
# len_city_1 = len(city1)
# len_city_2 = len(city2)
# len_city_3 = len(city3)
# if min(len_city_1, len_city_2, len_city_3) == len_city_1:
#     print(city1)
# elif min(len_city_1, len_city_2, len_city_3) == len_city_2:
#     print(city2)
# else:
#     print (city3)
# if max(len_city_1, len_city_2, len_city_3) == len_city_1:
#     print(city1)
# elif max(len_city_1, len_city_2, len_city_3) == len_city_2:
#     print(city2)
# else:
    # print(city3)

# a, b, c  = input(), input(), input()
# len_a = len(a)
# len_b = len(b)
# len_c = len(c)
# max1 = max(len_a, len_b, len_c)
# min1 = min(len_a, len_b, len_c)
# middle = (len_a + len_b + len_c) - max1 - min1
# if max1 - middle == middle - min1:
#     print ("YES")
# else:
#     print ("NO")

# a = input()
# if "суббота" in a or "воскресенье" in a:
#     print("YES")
# else:
#     print("NO")

# email = input()
# if "@" in email and "." in email:
#     print("YES")
# else:
#     print("NO")

# x1, y1, x2, y2  = float(input()), float(input()), float(input()), float(input())
# x = sqrt((x1-x2)**2 + (y1-y2)**2)
# print(x)

# r = float(input())
# s = pi * (r**2)
# c = 2*pi*r
# print(s)
# print(c)

# a = float(input())
# b = float(input())
# x1 = (a+b)/2
# x2 = sqrt(a*b)
# x3 = (2*a*b)/(a+b)
# x4 = sqrt((a**2 + b**2)/2)
# print (x1)
# print (x2)
# print (x3)
# print (x4)

# x = float(input())
# y = radians(x)
# x1 = sin(y) + cos(y) + (tan(y)**2)
# print(x1) 

# x = float(input())
# y = floor(x) + ceil(x)
# print (y)

# a = float(input())
# b = float(input())
# d1 = float(input())
# x1 = (-b - sqrt(b**2 - 4*a * d1))/(2*a)
# x2 = (-b + sqrt(b**2 - 4*a * d1))/(2*a)
# max1 = max(x1, x2)
# min1 = min(x1, x2)
# if x1 ==0 and x2 == 0:
#     print("Нет корней")
# elif x1 != x2:
#     print(min(x1, x2))
#     print(max(x1, x2))
# elif x1 == x2 and max1 != 0 or min1 != 0:
#     print(x1)

# elif min(x1, x2) == x1:
#     print(x1)
# elif min(x1, x2) == x2:
#     print(x2)
# elif max(x1, x2) == x1:
#     print(x1)
# elif max(x1, x2) == x2:
#     print(x2)



# # Ввод коэффициентов
# a = float(input())
# b = float(input())
# c = float(input())

# # Вычисление дискриминанта
# D = b**2 - 4*a*c

# # Анализ дискриминанта
# if D < 0:
#     print("Нет корней")
# elif D == 0:
#     x = -b / (2 * a)
#     print(x)
# else:
#     x1 = (-b + sqrt(D)) / (2 * a)
#     x2 = (-b - sqrt(D)) / (2 * a)
#     print(min(x1, x2))
#     print(max(x1, x2))

# n = int(input())
# a = float(input())

# s = (n*(a**2))/(4*tan(pi/n))
# print(s)

# n = int(input())
# for i in range (n):
#     print ("*" * 19)

# a = input()
# for i in range (10):
#     print (i, a)

# num = int(input())
# for i in range (num+1):
#     print ("Квадрат числа", i, "равен", i*i)

# n = int(input())
# if n >= 2:
#     for i in range (n):
#         print ("*" * (n - i)) # первый цикл будет 0, поэтому, например, "*" * 3 (3-0)

# Напишите программу, которая предсказывает размер популяции организмов с 1-го по 
# n-й день (включительно). Программа должна выводить номер дня, а затем через пробел размер популяции в этот день.
# m = int(input())
# p = int(input())
# n = int(input())
# for i in range(n):
#     print(i+1, m * (1+p/100)** i) # решение через сложный процент

# for i in range(100, 1000):  # перебираем числа от 100 до 999
#     if i % 10 == 7:         # используем остаток от деления на 10, для получения последней цифры
#         print(i)

# m = int(input())
# n = int(input())
# if m < n:
#     for i in range (m, n+1, 1):
#         print(i)
# else:
#     for i in range (m, n-1, -1):
#         print(i)

# m = int(input())
# n = int(input())
# for i in range (m, n+1):
#     print(i)
        # if i % 2 != 0:

# Даны два целых числа m и n (m>n). Напишите программу, которая 
# выводит все нечетные целые числа от m до n (включительно) в порядке убывания.
# m = int(input())
# n = int(input())
# for i in range (m, n-1, -1):
#     if i % 2 !=0:
#         print(i)


# Даны два натуральных числа (m≤n). Напишите программу, которая выводит все целые числа от 
# m до n (включительно), удовлетворяющие хотя бы одному из условий:
# число кратно 17
# число оканчивается на 9
# число кратно 3 и 5 одновременно

# m = int(input())
# n = int(input())
# if m <= n:
#     for i in range (m, n+1):
#         if i % 17 == 0:
#             print(i)
#         if i % 10 == 9:
#             print(i)
#         if i % 3 == 0 and i % 5 == 0:
#             print(i)    

# n = int(input())
# for i in range (0, 10):
#     x = n * (i+1)
#     print(n, "x", i+1, '=', x) 


# largest = 0
# for _ in range(10):
#     num = int(input())    
#     if num > largest:
#         largest = num

# print('Наибольшее число равно', largest) 

# largest = int(input())  # принимаем первое число за максимальное
# for _ in range(9):
#     num = int(input())
#     if num < largest:
#         largest = num

# print('Наибольшее число равно', largest) 

# выводит общую сумму 
# total = 0
# for i in range(1, 6):
#     total += i
# print(total)
# # 15

# # выводит каждое значение каждого цикла без пробелов
# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')
# # 1361015



# a = int(input())
# b = int(input())
# num = 0
# for i in range(a, b+1):
#     if i**3 % 10 == 4 or i**3 % 10 == 9:
#         num += 1
# print (num)

# n = int(input())
# num = 0
# for _ in range (n):
#     number = int(input())
#     num += number

# print (num)

# n = int(input())
# num = 0
# for i in range (1, n+1):
#     num += 1/i 
# print (num - log(n))

# На вход программе подается натуральное число n. 
# Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно), квадрат которых оканчивается на 2,5 или 8.

# n = int(input())
# num = 0
# for i in range(1, n+1):
#     if i**2%10==2 or i**2%10==5 or i**2%10==8:
#         num += i
# print (num) 

# Факториал. На вход программе подается натуральное число. Напишите программу, которая вычисляет n!
# n = int(input())
# num = 1
# for i in range (1, n+1):
#     num *= i
# print (num)

# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
# total = 1
# for _ in range (10):
#     n = int(input())
#     if n != 0:
#         total*=n
# print (total)

# На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.
# n = int(input())
# num = 0
# for i in range (1, n+1):
#     if n%i ==0:
#        num += i
# print (num)

# На вход программе подаётся натуральное число n. Напишите программу вычисления знакочередующейся суммы:
# 1−2+3−4+5−6+…+(−1)n+1⋅n
# n = int(input())
# num = 0
# for i in range (1, n+1):
#     if i%2 != 0:
#         num += i
#     else:
#         num -= i
# print (num)

# На вход программе подается натуральное число n, а затем nразличных натуральных чисел последовательности, 
# каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
# n = int(input())
# max1 = 0
# max2 = 0
# for i in range (1, n+1):
#     number = int(input())
#     if number > max1:
#         max2 = max1
#         max1 = number
#     elif number > max2:
#         max2 = number

# print (max1)
# print (max2)
    
# n = int(input())
# x = 0
# for i in range (1, 10+1):
#     number = int(input())
#     if number%2 == 0:
#         x = number + 1
#     else:
#         print("NO")       
# if i == 10:
#     print("YES")
# else:
#     print("NO")

# Напишите программу, которая считывает последовательность из 
# 10 целых чисел и определяет, является ли каждое из них чётным или нет.
# flag = True
# for i in range (1, 10+1):
#     number = int(input())
#     if number % 2 !=0:
#         flag = False
# if flag == False:
#     print("NO")
# else:
#     print("YES")

# Последовательность Фибоначчи
# n = int(input())
# a = 0
# b = 1
# for _ in range(1, n+1):
#     a, b = b, a + b
#     print(a, end=' ')


# i = 0
# while i < 10:
#     print('Привет')
#     i += 1

# text = input()
# total = 0
# while text != 'stop':
#     total += int(text)
#     text = input()

# print('Сумма чисел равна', total)

# i = 5
# while i <= 11:
#     print('Python awesome!')
#     i += 1

# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
# print(a)

# На вход программе подается последовательность слов, каждое слово на отдельной строке. 
# Концом последовательности является слово «КОНЕЦ» (без кавычек). 
# При этом само слово «КОНЕЦ» не входит в последовательность, лишь символизируя её окончание. 
# Напишите программу, которая выводит члены данной последовательности.
# or text != "конец"
# text = input()
# while text != "КОНЕЦ" and text != "конец": #или использовать NOT in ("КОНЕЦ", "конец")
#     print(text)
#     text = input()


# На вход программе подается последовательность слов, каждое слово на отдельной строке. 
# Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). 
# Сами эти слова в последовательность не входят, лишь символизируя её окончание. 
# Напишите программу, которая выводит общее количество членов данной последовательности.
# Программа должна вывести общее количество членов данной последовательности.

# text = input()
# x = 0
# while text not in ("стоп", "хватит", "достаточно"):
#     text = input()
#     x += 1
# print (x)

# На вход программе подается последовательность целых чисел делящихся на 7, 
# каждое число на отдельной строке. Концом последовательности является любое число, 
# не делящееся на 7 (само это число в последовательность не входит, лишь символизируя её конец). Напишите программу, которая выводит члены данной последовательности.
# num = int(input())
# while num%7==0:
#     print(num)
#     num = int(input())

# На вход программе подается последовательность целых чисел, каждое число на отдельной строке. 
# Признаком окончания последовательности является любое отрицательное число, при этом в саму последовательность оно не входит. 
# Напишите программу, которая выводит сумму всех членов данной последовательности.
# num = int(input())
# x = 0
# while num >= 0:
#     x += num
#     num = int(input())
# print(x)

# На вход программе подается последовательность целых чисел от 1 до 5, характеризующее оценку ученика, каждое число на отдельной строке. 
# Концом последовательности является любое неположительное число либо число, большее 5. Напишите программу, которая выводит количество пятерок.
# num = int(input())
# x = 0
# while 0 < num <=5:
#     if num == 5:
#         x += 1
#     num = int(input())
# print (x)

# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево. 
# К тому же ведьмак не принимает купюры, он принимает только чеканные монеты. 
# В мире ведьмака существуют монеты с номиналами 1,5,10,25.
# Напишите программу, которая определяет, какое минимальное количество чеканных монет нужно заплатить ведьмаку.
# num = int(input())
# x = 0
# while num >= 25:
#     x += 1
#     num = num - 25
# while 25 > num >= 10:
#     x += 1
#     num = num - 10
# while 10 > num  >= 5:
#     x += 1
#     num = num - 5
# while 5 > num  >= 1:
#     x += 1
#     num = num - 1
# print (x)

# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1

#     num = num // 10

# print(total)

# Дано натуральное число. 
# Напишите программу, которая выводит его цифры в столбик в обратном порядке.
# num = int(input())
# while num != 0:
#     print (num % 10)
#     num = num // 10

# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.
# num = int(input())
# while num != 0:
#     print (num % 10, end="")
#     num = num // 10

# Дано натуральное число n(n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры и выводит текст
num = int(input())
max1 = 9
min1 = 0
while num != 0:
    x = num % 10
    if x <= max1:
        max1 = x
    if x >= min1:
        min1 = x
    num = num // 10
    
print ("Максимальная цифра равна", min1)
print ("Минимальная цифра равна", max1)


