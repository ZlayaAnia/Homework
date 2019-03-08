# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

names = {} 
# names - зачаток нового словаря
for i in students :
    name = i['first_name']
    # Получаем колюч нового словаря из значения старого(Value)
    if names.get(name):
        names[name] +=1  
    # Получаем новое (Value), обращаемся через "словарь-ключ" к значению и увеличивает его, при необходимости
    else :
        names[name]=1  
for k in names:
    print(k,':',names[k])


# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
names = {} 
for i in students :
    name = i['first_name']
    if names.get(name):
        names[name] +=1  
    else :
        names[name]=1 
k = 0
for max_name, k  in names.items():
    if k>names[name] :
        print('Самое частое имя среди учеников:', max_name)
# ???

# # Пример вывода:
# # Самое частое имя среди учеников: Маша

# # Задание 3
# # Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [ {'first_name': 'Вася'}, {'first_name': 'Вася'}, ],
  [ {'first_name': 'Маша'}, {'first_name': 'Маша'},{'first_name': 'Оля'},]]

pup_in_sclass = []
for sclass in school_students:
    names = {}
    for pupil in sclass:
        name = pupil['first_name']
        if names.get(name):
            names[name] +=1 
        else :
            names[name] =1
    pup_in_sclass.append(names)
#print(pup_in_sclass)
for student in pup_in_sclass:
    i=0
    for max_name, k in student.items():
        if i<student[max_name]:
            i=student[max_name]
            print('Самое частое имя в классе', pup_in_sclass.index(student)+1,':', max_name)




# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
i=0
for ssclass in school:
    xy=0
    xx=0 
    for pupil in school[i]['students']: 
        for number, name in pupil.items():
            for fname, male in is_male.items():
                if name == fname:
                    if male == True:
                        xy+=1
                    else :
                        xx+=1
    print('В классе', school[i]['class'], 'девочек - ',xx,', мальчиков -',xy)
    i+=1

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# # По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

i=0
group=[]
for ssclass in school:
    group_male = {}
    xy=0
    xx=0 
    y=0
    for pupil in school[i]['students']: 
        for number, name in pupil.items():
            for fname, male in is_male.items():
                if name == fname:
                    if male == True:
                        xy+=1
                    else :
                        xx+=1
    y=(xx+xy)/(1+xx+xy)
    group_male.get(school[i]['class'])
    group_male[school[i]['class']]=y
    group.append(group_male)
    i+=1
for student in group:
    i=1
    for schclass, males in student.items():
        if i<=student[schclass]:
            print('Больше всего мальчиков в классе', schclass)
        else:
            print('Больше всего девочек в классе', schclass) 


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
