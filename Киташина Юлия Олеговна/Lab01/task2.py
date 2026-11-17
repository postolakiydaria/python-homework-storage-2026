#!/usr/bin/env python3

COURSES = ("Математический анализ", "Линейная алгебра", "Программирование", "Английский язык", "История", )


def main():
    while True:
        try:
            student_count = int(input("Введите количество студентов: "))
            if student_count > 0:
                break
            print("Количество студентов должно быть больше нуля.")
        except ValueError:
            print("Введите целое число.")

    all_grades = []

    for student_number in range(1, student_count + 1):
        while True:
            name = input(f"Введите имя студента №{student_number}: ").strip()
            if name != "":
                break
            print("Имя не может быть пустым.")
        grades = []

        for course in COURSES:
            while True:
                try:
                    grade = int(input(f"Оценка по курсу «{course}»: "))
                except ValueError:
                    print("Оценка должна быть целым числом от 3 до 5.")
                    continue

                if 3 <= grade <= 5:
                    grades.append(grade)
                    break
                print("Оценка должна быть от 3 до 5 включительно.")

        all_grades.extend(grades)
        average = sum(grades) / len(grades)
        print(f"{name}: средний балл — {average:.2f}")
        print("Минимальная оценка:", min(grades))
        print("Максимальная оценка:", max(grades))

    total_average = sum(all_grades) / len(all_grades)
    print(f"Средний балл по всем студентам: {total_average:.2f}")
    print("Минимальная оценка по всем студентам:", min(all_grades))
    print("Максимальная оценка по всем студентам:", max(all_grades))


if __name__ == "__main__":
    main()

    
