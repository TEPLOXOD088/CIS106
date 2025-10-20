# Problem 1: Compute rewards points

def compute_rewards(points, code):
    if code == "get":
        rewards = points * 1.5
    else:
        rewards = points
    print(f"Points: {points}")
    print(f"Redemption code: {code}")
    print(f"Rewards points: {rewards}")

# Example call
points = float(input("Enter points: "))
code = input("Enter redemption code: ")
compute_rewards(points, code)
