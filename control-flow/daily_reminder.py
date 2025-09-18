while True:
    task = input("Describe your task: ")
    priority = input("What is the task priority? (high, medium, low):  ")
    time_bound = input("Is it time-bound? yes or no: ")

    match priority:

        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a high priority task. Consider completing it when you have soon.")

        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires moderate attention anytime!")
            else:
                print(f"Note: '{task}' is a medium priority task. Consider completing it when you have free time.")

        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that requires low attention anytime!")
            else:
                print(f"Note: '{task}' is a low priority task. Take your time.")


        case _:
            print("Invalid input. Try again")
            continue
    break
    

print("Done")
