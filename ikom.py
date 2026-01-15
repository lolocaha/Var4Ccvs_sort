import csv
import os

owners= []
def test():#Функция для проверки csv файла и вывода его
    try:
        with open('po.csv','r',encoding='utf-8-sig') as f: #открываем файл
            csvreader = csv.DictReader(f,delimiter=',') #С помощью dictreader даем программе названия заголовков
            for row in csvreader: #проходим по каждому значению под заголовками
                record = {
                'Фамилия': row['Фамилия'],
                'Имя': row['Имя'],
                'Отчество': row['Отчество'],
                'Регистрационный номер': row['Регистрационный номер'],
                'Марка автомобиля': row['Марка автомобиля'],
                'Объем двигателя': float(row['Объем двигателя']),
                'Год выпуска': int(row['Год выпуска']),
                'Год постановки на учёт': int(row['Год постановки на учёт'])
                }
                owners.append(record)
    except FileNotFoundError:
        print('Файл не найден')
    except ValueError:
        print('Некорректные данные в файле')
    return owners
def bubble_sort(arr,zad): #сортировка пузырьком
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if zad(arr[j], arr[j + 1]):
                a = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = a
    return arr
def report1(owners):#Меню для 1 задания
    print('1.Все автовладельцы')
    def task1(a,b):
        if a['Год постановки на учёт'] != b['Год постановки на учёт']: #если значение не равны, то сортируем по убыванию
            return a['Год постановки на учёт'] < b['Год постановки на учёт']
        return a['Фамилия'] > b['Фамилия']#сортируем по возрастанию
    sorted_owners = owners.copy()#копируем список
    bubble_sort(sorted_owners,task1) #сортируем список
    with open('all_owners.csv',mode='w',newline='')as file:
        writer=csv.writer(file)
        for row in sorted_owners: #проходим по нему и выводим значения
            firsttask = []
            firsttask.append(row)
            writer.writerow(firsttask)
        if os.path.exists('all_owners.csv'):
            print('Файл all_owners создан')
    print('\n')

def report2(owners): #Меню для 2 задания
    print('2.Все владельцы автомобиля "ВАЗ"')
    vaz_owners = [] #Создаем список куда будут записываться люди с ВАЗ
    for row in owners:
        brand = row['Марка автомобиля']#находим строки, в которых есть автомобиль ВАЗ
        if brand.find('ВАЗ') != -1:
            vaz_owners.append(row)
    def task2(a,b):
        if a['Год выпуска'] != b['Год выпуска']: #если год выпуска не совпадает, сортируем по убыванию
            return a['Год выпуска'] < b['Год выпуска']
        if a['Объем двигателя'] != b['Объем двигателя']:#если объем двигателя не равен,то сортируем по возрастанию
            return a['Объем двигателя'] > b['Объем двигателя']
        return a['Фамилия'] > b['Фамилия']#сортируем по возрастанию

    if len(vaz_owners)  == 0:#если список пустой, то выведет, что таких автомобилистов нет
        print('Людей с таким автомобилем нет')
    else:
        bubble_sort(vaz_owners,task2)#сортируем и выводим значение
        with open('VAZ_owners', mode='w', newline='') as fi:
            writer=csv.writer(fi)
            for row in vaz_owners:
                secondtask = []
                secondtask.append(row)
                writer.writerow(secondtask)
            if os.path.exists('VAZ_owners.csv'):
                print('Файл VAZ_owners.csv создан')

def report3(owners):
    print('3.Список всех владельцев автомобилей с годом выпуска ранее заданного')
    year = input('Введите год:')#вводим год и проверяем является ли введенное значение числом
    if year.isdigit():
        limit_year = int(year)
    else:
        print('Некорректный ввод,будет использован 2010 год')
        limit_year = 2010
    old_cars = []
    for row in owners:
        if row['Год выпуска'] < limit_year:#находим строки, в которых год выпуска авто меньше введенного года
            old_cars.append(row)

    def task3(a,b): #функция для 3 задания
        if a['Год выпуска'] != b['Год выпуска']: #если год выпуска не равен, то сортируем по убыванию
            return a['Год выпуска'] < b['Год выпуска']
        return a['Марка автомобиля'] > b['Марка автомобиля']#сортируем по возрастанию
    if len(old_cars) == 0:#если количество строк равно 0, то таких автомобилистов нет
        print('Таких владельцев нет')
    else:
        bubble_sort(old_cars,task3)#сортируем и выводим значения
        with open('Old_cars_owners.csv', mode='w', newline='') as fil:
            writer=csv.writer(fil)
            for i in old_cars:
                old_cars_sort= []
                old_cars_sort.append(i)
                writer.writerow(old_cars_sort)
            if os.path.exists('Old_cars_owners.csv'):
                print('Файл Old_cars_owners.csv создан')

def main(): #Функция для интерфейса меню
    all_owners = test()
    if len(all_owners) < 25:
        print('В базе менее 25 записей')
    while True:
        print('\nМеню "Учет в ГИБДД"')
        print('1 - Полный список всех автовладельцев')
        print('2 - Список автовладельцев ВАЗ')
        print('3 - Список авто старше заданного года')
        print('0 - Выход')
        choice = input('Выберите пункт от 0 до 3: ').strip()
        if choice == '1':
            report1(all_owners)
        elif choice == '2':
            report2(all_owners)
        elif choice == '3':
            report3(all_owners)
        elif choice == '0':
            break
        else:
            print('Введите значение заново')
        print(input('Для продолжения нажмите Enter'))
if __name__ == '__main__':
    main()



