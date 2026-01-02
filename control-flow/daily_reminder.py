task_description = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority == "high":
    if time_bound == "yes":
        print(f"Reminder: {task_description} is a high priority task that requires immediate attention today!")
    else:
        print(f"Reminder: {task_description} is a high priority task.")
elif priority == "medium":
    if time_bound == "yes":
        print(f"Reminder: {task_description} is a medium priority task that is time-bound.")
    else:
        print(f"Reminder: {task_description} is a medium priority task.")
elif priority == "low":
    if time_bound == "yes":
        print(f"Reminder: {task_description} is a low priority task that is time-bound.")
    else:
        print(f"Reminder: {task_description} is a low priority task. Consider completing it when you have free time.")