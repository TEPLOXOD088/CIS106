# M7P3 - Collect student data with while loop

count = 0
choice = input("Do you want to enter student data? (Yes to continue): ").strip().lower()

while choice == "yes":
    last_name = input("Enter last name: ")
    score1 = float(input("Enter first exam score: "))
    score2 = float(input("Enter second exam score: "))
    avg = (score1 + score2) / 2
    print(f"Student: {last_name}, Average Score: {avg:.2f}")
    count += 1
    choice = input("Do you want to enter another student? (Yes to continue): ").strip().lower()

print(f"Total students entered: {count}")
