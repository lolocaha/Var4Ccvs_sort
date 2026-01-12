import csv
c = []
with open('po.csv','r',encoding='utf8') as f:
    csvreader = csv.DictReader(f,delimiter=',')
    for row in csvreader:
        record = {
        'Фамилия': row['\ufeffФамилия'],
        'Имя': row['Имя'],
        'Отчество': row['Отчество'],
        'Регистрационный номер': row['Регистрационный номер'],
        'Марка автомобиля': row['Марка автомобиля'],
        'Объем двигателя': float(row['Объем двигателя']),
        'Год выпуска': int(row['Год выпуска']),
        'Год постановки на учёт': int(row['Год постановки на учёт'])
        }
        c.append(record)
def bubble_sort(arr,zad):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if zad(arr[j], arr[j + 1]):
                a = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = a
    return arr
sorted_c = c.copy()
print('1.Все автовладельцы')
print('Сначала сортировка по году постановки на учет (по убыванию) , а затем по фамилиям (по возрастанию)')
def zad1(a,b):
    if a['Год постановки на учёт'] != b['Год постановки на учёт']:
        return a['Год постановки на учёт'] < b['Год постановки на учёт']
    return a['Фамилия'] > b['Фамилия']
bubble_sort(sorted_c,zad1)
for row in sorted_c:
    print(row)
print('\n')

print('2.Все владельцы автомобиля "ВАЗ"')
print('Сначала сортировка по году выпуска (по убыванию), потом по объему двигателя(по возрастанию), а затем по фамилии(по возрастанию)')
vaz = []
for row in c:
    brand = row['Марка автомобиля']
    if brand.find('ВАЗ') != -1:
        vaz.append(row)
def zad2(a,b):
    if a['Год выпуска'] != b['Год выпуска']:
        return a['Год выпуска'] < b['Год выпуска']
    if a['Объем двигателя'] != b['Объем двигателя']:
        return a['Объем двигателя'] > b['Объем двигателя']
    return a['Фамилия'] > b['Фамилия']

if len(vaz)  == 0:
    print('Людей с таким автомобилем нет')
else:
    bubble_sort(vaz,zad2)
    for row in vaz:
        print(row)
print('\n')
print('3.Список всех владельцев автомобилей с годом выпуска ранее заданного')
print('Сортировка по году выпуска (по убыванию) и по  марке автомобиля (по возрастанию)')
print('\n')
r = input('Введите год:')
if r.isdigit():
    l = int(r)
else:
    print('Вы ввели не число,будет использован 2010 год')
    l = 2010
year = []
for row in c:
    if row['Год выпуска'] < l:
        year.append(row)

def zad3(a,b):
    if a['Год выпуска'] != b['Год выпуска']:
        return a['Год выпуска'] < b['Год выпуска']
    return a['Марка автомобиля'] > b['Марка автомобиля']
if len(year) == 0:
    print('Таких владельцев нет')
else:
    bubble_sort(year,zad3)
    for i in year:
        print(i)


