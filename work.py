import ru_local

pys_str = str(input(ru_local.ONEWORD))
sogl_b = str(input(ru_local.TWOWORD))

one = sogl_b + 'а'
two = sogl_b + 'о'
three = sogl_b + 'э'
fore = sogl_b + 'и'
five = sogl_b + 'ы'
six = sogl_b + 'е'
seven = sogl_b + 'ё'
eight = sogl_b + 'ю'
nine = sogl_b + 'у'
ten = sogl_b + 'я'

one_str = pys_str.replace('а','а' + one)
two_str = one_str.replace('о','о' + two)
three_str = two_str.replace('э','э' + three )
fore_str = three_str.replace('и','и' + fore)
five_str = fore_str.replace('ы','ы' + five)
six_str = five_str.replace('е','е' + six)
seven_str = six_str.replace('ё','ё' + seven)
eight_str = seven_str.replace('ю','ю' + eight)
nine_str = eight_str.replace('у','у' + nine)
ten_str = nine_str.replace('я','я' + ten)

One_str = ten_str.replace('А','А' + one)
Two_str = One_str.replace('О','О' + two)
Three_str = Two_str.replace('Э','Э' + three )
Fore_str = Three_str.replace('И','И' + fore)
Five_str = Fore_str.replace('Ы','Ы' + five)
Six_str = Five_str.replace('Е','Е' + six)
Seven_str = Six_str.replace('Ё','Ё' + seven)
Eight_str = Seven_str.replace('Ю','Ю' + eight)
Nine_str = Eight_str.replace('У','У' + nine)
Ten_str = Nine_str.replace('Я','Я' + ten)

print('')
print(Ten_str)
print('............................................')
print('')


pys_str = str(input(ru_local.TREEWORD))
sogl_b = str(input(ru_local.TWOWORD))

one = sogl_b + 'а'
two = sogl_b + 'о'
three = sogl_b + 'э'
fore = sogl_b + 'и'
five = sogl_b + 'ы'
six = sogl_b + 'е'
seven = sogl_b + 'ё'
eight = sogl_b + 'ю'
nine = sogl_b + 'у'
ten = sogl_b + 'я'

one_str = pys_str.replace('а' + one, 'а')
two_str = one_str.replace('о' + two,'о')
three_str = two_str.replace('э' + three,'э')
fore_str = three_str.replace('и' + fore,'и')
five_str = fore_str.replace('ы' + five,'ы')
six_str = five_str.replace('е' + six,'е')
seven_str = six_str.replace('ё' + seven,'ё')
eight_str = seven_str.replace('ю' + eight,'ю')
nine_str = eight_str.replace('у' + nine,'у')
ten_str = nine_str.replace('я' + ten,'я')

One_str = ten_str.replace('А' + one,'А')
Two_str = One_str.replace('О' + two,'О')
Three_str = Two_str.replace('Э' + three,'Э')
Fore_str = Three_str.replace('И' + fore,'И')
Five_str = Fore_str.replace('Ы' + five,'Ы')
Six_str = Five_str.replace('Е' + six,'Е')
Seven_str = Six_str.replace('Ё' + seven,'Ё')
Eight_str = Seven_str.replace('Ю' + eight,'Ю')
Nine_str = Eight_str.replace('У' + nine,'У')
Ten_str = Nine_str.replace('Я' + ten,'Я')

print(Ten_str)
