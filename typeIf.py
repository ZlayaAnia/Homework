def stroka(strok1,strok2):
    if type(strok1)!=str or type(strok2)!=str:
        return '0'
    elif type(strok1)==str and type(strok2)==str and strok1==strok2 :
        return '1'
    elif type(strok1)==str and type(strok2)==str and strok1!=strok2 and len(strok1)>len(strok2) :
        return '2'
    elif type(strok1)==str and type(strok2)==str and strok1!=strok2 and str(strok2)==str('learn') :
        return '3'
    else :
        return 'LaLaLa'
  

strok1 = 123
strok2 = 3.14
print(strok1,' ',strok2)
print(stroka(strok1,strok2))

strok1 = 123
strok2 = 'hello'
print(strok1,' ',strok2)
print(stroka(strok1,strok2))
 
strok1 = 'hello'
strok2 = 'hello'
print(strok1,' ',strok2)
print(stroka(strok1,strok2))

strok1 = 'Buongiorno'
strok2 = 'hello'
print(strok1,' ',strok2)
print(stroka(strok1,strok2))

strok1 = 'hello'
strok2 = 'learn'
print(strok1,' ',strok2)
print(stroka(strok1,strok2))

strok1 = 'learn'
strok2 = 'Python'
print(strok1,' ',strok2)
print(stroka(strok1,strok2))