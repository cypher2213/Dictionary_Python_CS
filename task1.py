students = {
    "Vitaly_Prikhodko": ["вул. Шевченка 1", 12, 10],
    "Dmytro_Kropyvnytskyi": ["вул. Лесі Українки 3", 12, 10],
    "Mikhail_Romanenko": ["вул. Франка 7", 12, 11],
    "Maxim_Derizemlya": ["вул. Грушевського 2", 12, 9],
    "Victoria_Zhuk": ["вул. Центральна 4", 10, 10],
    "Andrey_Kuryanov": ["вул. Садова 9", 5, 10],
    "Oksana_Dubovets": ["вул. Вишнева 6", 7, 11],
    "Nikita_Stroganov": ["вул. Миру 8", 6, 10],
    "Karina_Nikolaenko": ["вул. Квіткова 10", 2, 11],
    "Eugenia_Dron": ["вул. Коцюбинського 5", 12, 11]
}

target_school = int(input("Введіть номер школи: "))
result = []

for name, data in students.items():
    address, school_number, grade = data
    if school_number == target_school and grade in (10, 11):
        first_name, last_name = name.split("_")
        result.append({last_name: (first_name, address)})


if result:
    print("\nУчні старших класів обраної школи:")
    for item in result:
        print(item)
else:
    print("Учнів старших класів у цій школі не знайдено.")
