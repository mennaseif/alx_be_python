task = input ("Enter the task: ")
priority = input ("Priority (high/medium/low): ").lower()
time_bound =input ("Is it time bound? (yes/no): ").lower()

match priority:
    case "hight":
        if time_bound == "yes":
           print (f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else :
             print (f"Reminder: {task} is a high priority task. Try to complete it soon.")   
    case "medium":
        if time_bound == "yes":
           print (f"Reminder: {task} is a medium priority task that requires immediate attention today!")
        else :
             print (f"Reminder: {task} is a medium priority task. Try to complete it this week.") 
    case "low":
        if time_bound == "yes":
           print (f"Reminder: {task} is a low priority task that requires immediate attention today!")
        else :
             print (f"Reminder: {task} is a low priority task. Try to complete it at your free time.") 
    case _:
        print ("Invalid priority entered. Please enter high, medium, or low.")         
 