#6-й день: 3,22
#Ответ: на 6-й день спортсмен достиг результата - не менее 3 км.

a = int(input("Введите сколько спортсмен пробежал за день:"))
b = int(input("Предельный пробег:"))

number = 1
while a < b:
    a *= 1.1
    number += 1
    print(f'Количество дней за которое перевалит через заданный километраж {number}')