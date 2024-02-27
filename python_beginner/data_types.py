# 8 основных типов данных

#1)int целый числовой тип данных:
#    a) float- числа с плавающией точкой
#    b) complex-  числа с буквенным вырожением(123456п)
# 2)str - строковой тип данных
# 3)bool - буквенный тип данных \ логический(true folse)
# 4)list - список[]
# 5)tuple - кортеж \ не изменяемый список()
# 6)set - множество {}
# 7)dict - словарь {}
# 8)NoneType - тип данных для обозночениия отсутствия значения (None)


# изменяемые типы данных 
#(list)
#(dict)
#(set)

#print("") - функция для вывода терминала
""" print("hello world")
name = input ("введите ваше имя:") """

""" print ("салам алейкум, " + name) """

""" print("привет\n как дела")

str1 = "hello"
str2= "world"
print(str1 + str2)
 """
""" frog = 'quak'
print (frog *3)  """

""" функции и методы строк """

""" greeting = "добрый вечер" """

#print(len(greeting))
#len(x) - возврощает количество элементов

""" print(dir(greeting)) """
# dir(x) - возврощает список методом переданного обьектов
# метод - функция, пренадлежащая определенному типу данных, и может быть вызван только через обьект

""" my_str = 'HELLO#WORLD'
print(my_str.lower())
print(my_str.upper())
print(my_str.replace('#', ' ')) """
""" print(my_str.split)# """


""" my_str2.title()#Hello World
my_str2.capitalize()#Hello world
my_str2.count("l")# 3
print(my_str2.strip())#удаление лишних пробелов
my_str2.lstrip()
my_str2.rstrip() """

""" my_str2 = '   hello world    ' 
print(my_str2.strip('!')) """

my_str3 = 'my new String'
""" 
my_str3.isalpha()# true
my_str3.isdiqit()# folse
my_str3.isolnum()# folse
my_str3.startwith('M')#true
my_str3.endswith('M')#folse
 """
# in

""" my_str4 = 'hello world'

print('hello' in my_str4)
 """
#'hello' in my_str4 # true

name = input('имя:')
party = input('вечеринка:')

""" invite1 = 'дорогой %s, приглашаем тебя на %s' %(name, party)
print(invite1) """
""" invite2 = 'дорогой{a1}, приглашаем тебя на {b2}' format(a1=name,b2=party)
print(invite2) """


invite3 = f'дорогой{name} приглашаем тебя на {party}'
print(invite3)

string = 'python'

