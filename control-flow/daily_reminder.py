task_description = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task_description}' is a high priority task"
    case "medium":
        reminder = f"'{task_description}' is a medium priority task"
    case "low":
        reminder = f"'{task_description}' is a low priority task"
    case _:
        reminder = "Invalid priority level entered."
    
if time_bound == "yes":
    reminder += " that requires immediate attention today!" 
    print(f"Reminder: {reminder}")
else:
    print(f"Note: {reminder}. Consider completing it when you have free time.")