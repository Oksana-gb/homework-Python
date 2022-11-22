import csv

db_main=dict()
global_mapping=['фамилия','имя', 'класс']


# создаем запись
def create_record(db:dict, data:list, mapping:list)-> dict:     
    a=1 if len(db)<1 else max(db, key = lambda i: int(i))+1          
    db[a]={name:value for name, value in zip(mapping,data)}
    return db


# выводим в консоль по id
def read_record(db:dict, rec_id)->dict:
    print(db[rec_id])


# Обновить запись по ID
def update_record(db:dict, rec_id, data:list, mapping:list)-> dict:
    db[rec_id]={name:value for name, value in zip(mapping,data)}
    return db


# Удалить запись по ID
def delete_record(db:dict, rec_id)->dict:
    del db[rec_id]


# записываем в файл
def export(db:dict, file)->None:

    with open(file, 'w', encoding="utf8") as csvfile:
        header=['id','фамилия','имя', 'класс']
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        a=list(db.keys())
        for el in a:
            b=db[el]
            writer.writerow({'id':el,'фамилия':b['фамилия'], 'имя':b['имя'], 'класс':b['класс']})


# находим последнюю id и выдаем следующую свободную
def get_id(file):
    with open (file,'r', encoding="utf8") as data:
        for line in data:
            number=int(line)+1
    return number
  

# сохраняем id последней записи в файл
def store_id(db:dict, file)-> None:
    with open (file,'w', encoding="utf8") as data:
        a=max(db, key = lambda i: int(i))
        data.write(str(a))


# импортируем из файла в словарь (id уже есть)
def import_dict(file):
    with open(file, 'r', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            print(line['id'], line['фамилия'], line['имя'], line['класс'])


# импортируем из файла в словарь (id нет)
def import_without_id (db:dict, file:str, mapping:list, rec_id)->dict:
    with open(file, 'r', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            a=line['фамилия'], line['имя'], line['класс']
            db[rec_id]={name:value for name, value in zip(mapping,a)}
            rec_id+=1
    return db
        
