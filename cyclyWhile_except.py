dialog = {
    'Как дела?':'Хорошо',
    'Что делаешь?' : 'Изучаю Python',
    'Как погода?' : 'Хочется тепла',
    'Как настроение?': 'Сонливое',
    'Где вчера был?' : 'Как обычно - на работе',
    'О чем думаешь?' :  'О горах и море',
 }
def user_say_to_mac(user_ask,dialog) :
    return dialog.get(user_ask)
def user_ask_mac(dialog):
    while True :
        user_ask = input('Спроси меня что-нибудь :) ')
        for user_ask in dialog.keys :
            dialog = user_say_to_mac(user_ask,dialog) 
            print(dialog) 
            if user_ask == 'Пока!':
                print('Пора спать, до встречи!') 
                break
try :

    while True:
        user_say = input('Как дела? ')
        if user_say == 'Хорошо' or user_say == 'хорошо':
            print('И у меня!) ')
            break
        else:
            print('Улыбнись! :)')
    user_ask_mac(dialog)
except KeyboardInterrupt :
    print('До встречи!')    
    

