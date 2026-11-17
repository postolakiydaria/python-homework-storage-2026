#!/usr/bin/env python3

COURSES = ('ВышМат', 'Физика', 'Программирование', 'История', 'Ботаника')

if __name__ == '__main__':
    students = {}
    while True:
        name = input("Введите Имя студента (если студенты закончились - напиши 'стоп')\n")

        if name.lower() == 'стоп':
            break

        if not name:
            print('Плохо! Имя не может быть пустым!')
            continue

        students[name] = {}

        for course in COURSES:
            while True:
                try:
                    score = int(input(f"Введите целое число от 3 до 5 {course}: "))
                    if 3 <= score <= 5:
                        students[name][course] = score
                        break
                    else:
                        print('Плохо! нужно ввести положительную оценку! Попробуйте снова.')
                except ValueError:
                    print("Плохо! Была введена билиберда!")
    if not students:
        print("Плохо! Нет студентов!")
    else:
        all_scores = [score for scores in students.values() for score in scores.values()]
        sr_score = sum(all_scores)/len(all_scores)
        min_score = min(all_scores)
        max_score = max(all_scores)

        print("--" *40)
        print(f'Всего оценок выставлено: {len(all_scores)}')
        print(f'Средний балл по всем студентам: {sr_score}')
        print(f'Минимальная оценка: {min_score}')
        print(f'Максимальная оценка: {max_score}')
