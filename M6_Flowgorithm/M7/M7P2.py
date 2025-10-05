# M7P2 - User enters start, stop, increment; display numbers

start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
step = int(input("Enter increment value: "))

num = start
while num <= stop:
    print(num)
    num += step
