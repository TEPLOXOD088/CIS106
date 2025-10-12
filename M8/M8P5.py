total_tuition = 0
count = 0

with open("students.txt") as file:
    lines = file.readlines()

for i in range(0, len(lines), 3):
    name = lines[i].strip()
    code = lines[i+1].strip()
    credits = int(lines[i+2].strip())
    if code == "I":
        tuition = credits * 250
    else:
        tuition = credits * 500
    total_tuition += tuition
    count += 1
    print(name, credits, tuition)

print("Total tuition owed:", total_tuition)
print("Number of students:", count)
