"""
Author: Nicole Diamantino
Assignment: #1
"""

# Step b: Create 4 variables

# string
gym_member = "Alex Alliton"  # str

# float
preferred_weight_kg = 20.5  # float

# integer
highest_reps = 25  # int

# boolean
membership_active = True  # bool

# Step c: Create a dictionary named workout_stats
# Dictionary storing friends and workout minutes as tuples
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 30, 50),
    "Taylor": (25, 35, 40)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, minutes in list(workout_stats.items()):
    total = sum(minutes)
    workout_stats[friend + "_Total"] = total

# Step e: Create a 2D nested list called workout_list
# 2D list containing workout minutes only
workout_list = [minutes for minutes in workout_stats.values()
                if isinstance(minutes, tuple)]

# Step f: Slice the workout_list
print("Yoga and Running minutes:")
for row in workout_list:
    print(row[:2])

print("\nWeightlifting minutes for last two friends:")
for row in workout_list[-2:]:
    print(row[2])

# Step g: Check if any friend's total >= 120
for key, value in workout_stats.items():
    if key.endswith("_Total") and value >= 120:
        name = key.replace("_Total", "")
        print(f"Great job staying active, {name}!")

# Step h: User input to look up a friend
friend_name = input("\nEnter a friend's name: ")

if friend_name in workout_stats:
    minutes = workout_stats[friend_name]
    total = workout_stats[friend_name + "_Total"]
    print("Workout minutes:", minutes)
    print("Total minutes:", total)
else:
    print(f"Friend {friend_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {k.replace("_Total", ""): v
          for k, v in workout_stats.items() if k.endswith("_Total")}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print("\nHighest total workout minutes:", highest_friend)
print("Lowest total workout minutes:", lowest_friend)
