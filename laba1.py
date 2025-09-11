# Лабораторна робота №1
# Створення змінних
name = 'Sasha'                              #тип даних str
age = 16                                    #тип даних int
height = 1.73                            #тип даних float
student = True                              #тип даних bool
hobbies = ['travel', 'dance']               #тип даних list
friends = {'Liza, Vlada, Alina'}                    #тип даних set
numbers = (1, 5, 6,3)                       #тип даних tuple
info =  {'country': 'Spain'}                   #тип даних dict

#виведення кожної змінної та її типу

print('name', type(name),':', name)
print('age', type(age),':', age)
print('height', type(height),':', height)
print('student', type(student),':', student)
print('hobbies', type(hobbies),':', hobbies)
print('friends', type(friends),':', friends)
print('numbers', type(numbers),':', numbers)
print('info', type(info),':', info)

a = 97
b = 5

c = a + b                #додавання
print(c)

d = a - b                #віднімання
print(d)

i = a * b                 #множення
print(i)

f = a / b                 #діленння (результат завжди float)
print(f)

g = a // b                #ділення без остачі
print(g)

j = a % b                 #остача від ділення
print(j)

k = a ** b                #піднесення до степення
print(k)
