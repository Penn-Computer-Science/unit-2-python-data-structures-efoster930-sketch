set = True
gradebook = {
    "OsamaSon":[86,88,83],
    "Yeat":[78,80,75],
    "Carti":[93, 95, 89]
    }

result = {}

while set == True:
    student_add = input("Want to add student and give them a grade? (Y/N) ").upper()
    if student_add == "Y":
        student_name = input("Name of the student? ")
        student_grades = input("Enter 3 grades separated by spaces ")
        list_grades = [int(x) for x in student_grades.split()]
        gradebook[student_name] = list_grades
        print(f"Student added successfully: {student_name} with grades {list_grades}")
        print(gradebook)
    elif student_add == "N":
        summary_grade = input("Want to look at the gradebook summary? (Y/N) ").upper()
        if summary_grade == "Y":
            for key, grades in gradebook.items():
                grade_sum = sum(grades)
                divided_grade = grade_sum / 3
                result[key] = divided_grade
                if divided_grade <= 60:
                    grade = "F"
                elif divided_grade > 60 and divided_grade <= 69:
                    grade = "D"
                elif divided_grade > 69 and divided_grade <= 79:
                    grade = "C"
                elif divided_grade > 79 and divided_grade <= 89:
                    grade = "B"
                elif divided_grade > 89 and divided_grade <= 100:
                    grade = "A"
                print(f"{key}:{grades}: {result[key]:.2f}")
                print(f"{key}'s grade: {grade}")
                max_key = max(result, key=result.get)
                print(f"Top student: {max_key}")
                sortinhg = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
                print(f"Sorted students: {sortinhg}")
        elif summary_grade == "N":
            remove_student = input("Want to remove to student? (Y/N) ").upper()
            if remove_student == "Y":
                the_student = input(f"What student you want to remove?: {list(gradebook.keys())} ")
                del gradebook[the_student]
                print(gradebook)
            elif remove_student == "N":
                exit_choice = input("Want to exit? (Y/N) ").upper()
                if exit_choice == "Y":
                    set = False
                elif exit_choice == "N":
                    set = True