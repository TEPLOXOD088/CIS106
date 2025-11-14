def main():
    students = {}
    count = int(input("How many students? "))
    for i in range(count):
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        students[name] = grade

    print("Name\tGrade")
    print("----\t-----")

    total = 0.0
    for name, grade in students.items():
        print(name + "\t" + str(grade))
        total = total + grade

    if count > 0:
        avg = total / count
    else:
        avg = 0.0

    print("Class average:", avg)

main()
