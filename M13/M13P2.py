def compute_grade_averages(student_grades):
    # student_grades: {name: [g1, g2, g3]}
    total1 = 0.0
    total2 = 0.0
    total3 = 0.0
    count = 0
    for grades in student_grades.values():
        total1 = total1 + grades[0]
        total2 = total2 + grades[1]
        total3 = total3 + grades[2]
        count = count + 1
    if count > 0:
        avg1 = total1 / count
        avg2 = total2 / count
        avg3 = total3 / count
    else:
        avg1 = 0.0
        avg2 = 0.0
        avg3 = 0.0
    return [avg1, avg2, avg3]

def main():
    students = {}
    count = int(input("How many students? "))
    for i in range(count):
        name = input("Enter student name: ")
        g1 = float(input("Enter grade 1: "))
        g2 = float(input("Enter grade 2: "))
        g3 = float(input("Enter grade 3: "))
        students[name] = [g1, g2, g3]

    print("Name\tAverage")
    print("----\t-------")
    for name, grades in students.items():
        total = 0.0
        for g in grades:
            total = total + g
        avg = total / 3.0
        print(name + "\t" + str(avg))

    class_avgs = compute_grade_averages(students)
    print()
    print("Class average for grade 1:", class_avgs[0])
    print("Class average for grade 2:", class_avgs[1])
    print("Class average for grade 3:", class_avgs[2])

main()
