#!/usr/bin/env python3

COURSES = ("Вышсшая Математика", "Физика", "Структуры Данных", "Органическая Химия", "Физическая Химия")

def journal(COURSES):
    students = {}
    while True:
        names = input("Введите ФИО студентов:")
        if not names:
            break
        if not names.replace(" ", "").isalpha():
            print("Ошибка! ФИО должно содержать только буквы!")
            continue
        grades = []
        for subject in COURSES:
            while True:
                try:
                    subject_grade = int(input(f"Оценка за дисциплину '{subject}':"))
                    if 3 <= subject_grade <= 5:
                        grades.append(subject_grade)
                        break
                    else: 
                        print("Ошибка ввода оценки за дисциплину. Попробуйте снова:")
                except ValueError:
                    print("Ошибка! Введите ЦЕЛОЕ число от 3 до 5.")
        students[names] = grades
    return students

if __name__ == "__main__":
    students = journal(COURSES) 

    if not students:
            print("Не был совершен ввод студентов.")
    else: 
        all_grades = []
        for names in students:
            all_grades.extend(students[names])

        average_grade = sum(all_grades) / len(all_grades)
        min_grade = min(all_grades)
        max_grade = max(all_grades)

        print(f"Всего введено студентов: {len(students)}")
        print(f"Средний балл по дисциплинам: {average_grade}")
        print(f"Минимальная оценка: {min_grade}")
        print(f"Максимальная оценка: {max_grade}")
