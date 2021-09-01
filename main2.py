employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']
names = [item.split()[-1] for item in employees]
for i in names:
    print('Привет,', i.title(), '!')
