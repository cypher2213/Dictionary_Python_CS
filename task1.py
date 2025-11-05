
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



def print_all_students(data):
    print("\nСписок усіх учнів:")
    for name, info in data.items():
        print(f"{name}: адреса - {info[0]}, школа №{info[1]}, клас {info[2]}")


def add_student(data):
    name = input("Введіть ім’я_прізвище (наприклад, Ivan_Petrenko): ")
    address = input("Введіть адресу: ")
    school = int(input("Введіть номер школи: "))
    grade = int(input("Введіть клас: "))
    data[name] = [address, school, grade]
    print(f"✅ Додано учня {name}")


def remove_student(data):
    name = input("Введіть ім’я_прізвище учня, якого потрібно видалити: ")
    if name in data:
        del data[name]
        print(f"🗑️ Учня {name} видалено.")
    else:
        print(f"⚠️ Учня {name} не знайдено.")


def print_sorted_students(data):
    print("\nУчні за алфавітом:")
    for name in sorted(data.keys()):
        info = data[name]
        print(f"{name}: адреса - {info[0]}, школа №{info[1]}, клас {info[2]}")


def find_senior_students_by_school(data):
    target_school = int(input("\nВведіть номер школи: "))
    result = []
    for name, info in data.items():
        address, school_number, grade = info
        if school_number == target_school and grade in (10, 11):
            first_name, last_name = name.split("_")
            result.append({last_name: (first_name, address)})

    if result:
        print("\nУчні старших класів обраної школи:")
        for item in result:
            print(item)
    else:
        print("Учнів старших класів у цій школі не знайдено.")



def main():
    while True:
        print("\n=== МЕНЮ ===")
        print("1. Вивести всіх учнів")
        print("2. Додати учня")
        print("3. Видалити учня")
        print("4. Переглянути учнів за алфавітом")
        print("5. Знайти учнів старших класів у школі")
        print("0. Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            print_all_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            remove_student(students)
        elif choice == "4":
            print_sorted_students(students)
        elif choice == "5":
            find_senior_students_by_school(students)
        elif choice == "0":
            print("👋 Програму завершено.")
            break
        else:
            print("⚠️ Невірний вибір, спробуйте ще раз.")



if __name__ == "__main__":
    main()
