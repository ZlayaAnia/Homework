# # Задание 1
# # Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
# students = [
#   {'first_name': 'Вася'},
#   {'first_name': 'Петя'},
#   {'first_name': 'Маша'},
#   {'first_name': 'Маша'},
#   {'first_name': 'Петя'},
# ]

# names = {} 
# # names - зачаток нового словаря
# for i in students :
#     name = i['first_name']
#     # Получаем колюч нового словаря из значения старого(Value)
#     if names.get(name):
#         names[name] +=1  
#     # Получаем новое (Value), обращаемся через "словарь-ключ" к значению и увеличивает его, при необходимости
#     else :
#         names[name]=1  
# for k in names:
#     print(k,':',names[k])


# # Пример вывода:
# # Вася: 1
# # Маша: 2
# # Петя: 2


# # Задание 2
# # Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# names = {} 
# for i in students :
#     name = i['first_name']
#     if names.get(name):
#         names[name] +=1  
#     else :
#         names[name]=1 
# k = 0
# for max_name, k  in names.items():
#     if k>names[name] :
#         print('Самое частое имя среди учеников:', max_name)
# # ???

# # # Пример вывода:
# # # Самое частое имя среди учеников: Маша

# # # Задание 3
# # # Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# school_students = [
#   [ {'first_name': 'Вася'}, {'first_name': 'Вася'}, ],
#   [ {'first_name': 'Маша'}, {'first_name': 'Маша'},{'first_name': 'Оля'},]]

# pup_in_sclass = []
# for sclass in school_students:
#     names = {}
#     for pupil in sclass:
#         name = pupil['first_name']
#         if names.get(name):
#             names[name] +=1 
#         else :
#             names[name] =1
#     pup_in_sclass.append(names)
# #print(pup_in_sclass)
# for student in pup_in_sclass:
#     i=0
#     for max_name, k in student.items():
#         if i<student[max_name]:
#             i=student[max_name]
#             print('Самое частое имя в классе', pup_in_sclass.index(student)+1,':', max_name)


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# school = [
#   {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
#   {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
# ]
# is_male = {
#   'Маша': False,
#   'Оля': False,
#   'Олег': True,
#   'Миша': True,
# }

# for ssclass in school:
#   xy=0
#   xx=0
#   for name in ssclass['students']: 
#     if is_male.get(name['first_name']):
#         xy+=1
#     else :
#         xx+=1
#   print('В классе', ssclass['class'], 'девочек - ',xx,', мальчиков -',xy)


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# # По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.

school = [
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}]},
  {'class': '4a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Оля'},{'first_name': 'Олег'}]},
  {'class': '5c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}, {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]}
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

boy=0
girl=0
boy_class=''
girl_class=''
for school_class in school:
  xy=0
  xx=0
  for name in school_class['students']:
    if is_male.get(name['first_name']):
      xy+=1
    else:
      xx+=1
  if boy<xy:
    boy=xy
    boy_class=school_class['class']
  if girl<xx:
    girl=xx
    girl_class=school_class['class']
  print('В классе', school_class['class'], 'девочек - ',xx,', мальчиков -',xy)
  #  строка вывода количества девочек/мальчиков - для удобства проверки
print('Больше всего мальчиков в классе',boy_class)
print('Больше всего девочек в классе',girl_class)

# Тут хотела сделать поиск класса с мах мальчиками/девочками, 
# но не получается обновлять max_pupil, max_pupil_class, поэтому белеберда выходит
# 
# def amount(pupil, pupil_class, max_pupil, max_pupil_class):
#   if max_pupil<pupil:
#     max_pupil = pupil
#     max_pupil_class = pupil_class
#   return max_pupil_class
# boy=0
# girl=0
# boy_class=''
# girl_class=''
# for school_class in school:
#   xy=0
#   xx=0
#   for name in school_class['students']:
#     if is_male.get(name['first_name']):
#       xy+=1
#     else:
#       xx+=1
# print('Больше всего мальчиков в классе', amount(xy, school_class['class'], boy, boy_class))
# print('Больше всего девочек в классе', amount(xx, school_class['class'], girl, girl_class))