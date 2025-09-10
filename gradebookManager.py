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
        print(gradebook)
    elif student_add == "N":
        summary_grade = input("Want to look at the gradebook summary? (Y/N)")
        if summary_grade == "Y":
            for key, grades in gradebook.items():
                grade_sum = sum(grades)
                divided_grade = grade_sum / 3
                result[key] = divided_grade
                print(result)




