def old(age):
 if  age>0 and age<7:
     return 'Вы ходите в детский сад'
 elif age>=7 and age<18:
    return 'Вы - школьник'
 elif age>=18 and age<25:
    return 'Возможно вы - студент'
 elif age>=25 and age<60:
    return 'Вероятнее всего вы работаете'   
 elif age>=60:
    return 'Пора на пенсию'
 else :
    return 'Вас ещё нет'

def god_goda(age):
 if  (int(age//10))!=1 and (int(age%10))==2 or (int(age%10))==3 or (int(age%10))==4:
     return '{}{}{}'.format('Вам ', age, ' года.')
 elif (int(age//10))!=1 and (int(age%10))==1:
     return '{}{}{}'.format('Вам ', age, ' год.')
 else :
    return '{}{}{}'.format('Вам ', age, ' лет.')

end = 1
while end==1 :
 age = int(input('Сколько вам полных лет? '))
 print(god_goda(age),old(age))
 end = int(input('1 - повторить, другая цифра - выход '))
