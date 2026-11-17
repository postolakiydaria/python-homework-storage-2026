COURSES = ("Высшая математика", "Дискретная математика",
           "Зоология беспозвоночных", "Анатомия и физиология",
           "История России")

def get_grade(course_name):
    while True:
            grade_str = input('Введите оценку за курс по дисциплине ', course_name)
            try:
                  grade = int(grade_str)
                  if grade >= 3 and grade <= 5:
                        return grade
                  else: 
                        print("Оценка должна быть не меньше тройки(удовлетворительно)")
            except ValueError:
                  print("Введите целое число")

def get_grades(courses):
    grades = {}
    for course in courses:
        grade = get_grade(course)
        grades[course] = grade 
    return grades

def add_students(students_data, name, grades):           
      students_data[name] = grades
      return students_data

def calculate(students_data):
      total_sum = 0
      total_count = 0
      for student in students_data:
            for grade in students_data[student].values():
                  total_sum += grade
                  total_count += 1
                if total_count == 0:        #чтобы не делить на ноль
                    return 0
                return total_sum/total_count        #return сдвинут и теперь функция идет по всем оценкам, а не по одной

def find_min_max(students_data):
      all_grades = []
      for students in students_data:
            for grade in students_data[students].values():
                  all_grades.append(grade)
            return (min(all_grades), max(all_grades))


def print_res(students_data):
      average = calculate(students_data)
      (min_grade, max_grade) = find_min_max(students_data)
      print("Средний балл:", average)
      print("Минимальная оценка:", min_grade)
      print("Максимальная оценка:", max_grade)

if __name__ == "__main__":
      #все курсы теперь находятся в начале кода
      students_data = {}

      while True:
            name = input("Введите имя студента: ")
            grades = get_grades(COURSES)
            students_data = add_students(students_data, name, grades)

            answer = input("Добавить ещё студента?(да или нет): ")

            if answer == "нет":
                  break
        print_res(students_data)      #поправлено 

