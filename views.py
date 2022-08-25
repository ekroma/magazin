import json
from sys import flags
FILE_PATH = 'data.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def catalog(i):
    print(f'''
        ID         : {i["id"]}
        Марка      : {i["mark"]}
        Модель     : {i["model"]}
        Год выпуска: {i["year"]}
        Описание   : {i["discription"]}
        Цена       : {i["price"]}
        '''   
    )

def listing():
    with open(FILE_PATH,'r') as file:
         for i in eval(file.read()):
            catalog(i)

def retrieve_product():
    data = get_data()

    id = int(input('Enter id: '))
    product = (list(filter(lambda x: x['id'] == id, data)))

    for i in product:
        catalog(i)
        
    if not product:
        return 'такого продукта нет'

def get_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())
        id += 1
    with open('id.txt', 'w') as file:
        file.write(str(id))
    return id

def create_product():
    data = get_data()
    try:    
        product = {
            'id'   : get_id(),
            'mark' : input('Введите марку продукта: '),
            'model': input('Введите модель продукта: '),
            'year' : int(input('Введите дату выпуска продукта:')),
            'discription': input('Введите описание продукта: '),
            'price': round(float(input('Введите цену продукта: ')), 2)
            }

    except ValueError:
        print()
        print('Вы ввели неверные данные!')
        print()
        create_product()
    else:
        data.append(product)
        with open(FILE_PATH, 'w') as file:
            json.dump(data, file,indent=2)
            catalog(product)
    return 'Создан'

def update_product():
    data = get_data()
    flag = False

    id = int(input('Введите id продукта: '))
    product = list(filter(lambda x: x['id'] == id, data))

    if not product:
        return 'Такого продукта нет'

    index_ = data.index(product[0])
    choice_ = int(input('что вы хотите изменить? 1 - Марка, 2 - Модель, 3 - описание, 4 - год выпуска, 5 - цена: '))

    if choice_ == 1:
        data[index_]["mark"] = input('Введите новую марку: ')
        flag = True

    elif choice_ == 2:
        data[index_]["model"] = input('Введите новую модель: ')
        flag = True

    elif choice_ == 3:
        data[index_]["year"] = input('Введите новую дату выпуска: ')
        flag = True

    elif choice_ == 4:
        data[index_]["discription"] = input('Введите новое описание: ')
        flag = True

    elif choice_ == 5:
        data[index_]["price"] = input('Введите новую цену: ')
        flag = True

    else:
        print('Такого поля нет')

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)

    if flag:
        return 'ОБНОВЛЕНО'
    else:
        return 'НЕ ОБНОВЛЕНО'

def delete_product():
    data = get_data()

    id = int(input('Введите id продукта для удоления: '))
    product = list(filter(lambda x: x['id'] == id, data))

    if not product:
        return 'Такого продукта нет'
        
    index_ = data.index(product[0])
    data.pop(index_)

    json.dump(data, open(FILE_PATH, 'w'))

    return 'УДАЛЕНО'