#initialising the empty list for storing the tasks
task = []
print("To-do List by B Chaitanya Reddy")
print("Follow the below instructions for successful usage of the to-do list\n")
print("select any of the choice based on your requirement\n")
# instructions to be followed for successful usage of To-do list
print("For adding the tasks, enter your choice as 1\n")
print("For viewing the entered tasks, enter your choice as 2\n")
print("For updating the tasks, enter your choice as 3\n")
print("For appending the new tasks, enter your choice as 4\n")
print("For removing tasks, enter your choice as 5\n")
print("For exit, enter your choice as 6\n")
# initialising the while loop until the user desires to exit the program
while True:
    user_choice=int(input("Enter your choice:"))#accepting the user's choice
    # initialising the if condition based on user's choice for adding the tasks into the to-do list
    if user_choice==1:
        n=int(input("Enter the number of tasks:"))
        for i in range(n):
            task.append(input(f"Task {i+1}:"))
    # initialising the elif condition based on user's choice to display the tasks in the to-do list
    elif user_choice==2:
        if task:
            for i, t in enumerate(task, 1):
                print(f"Task {i}: {t}")
        else:
            print("No tasks available.\n")
    # initialising the elif condition based on user's choice for updating the tasks in the to-do list
    elif user_choice==3:
        for i, t in enumerate(task, 1):
            print(f"{i}. {t}")
        task_num=int(input("Enter the number of the task to be updated: ")) - 1
        if 0<=task_num<len(task):
            updated_task=input("Enter the updated task: ")
            task[task_num]=updated_task
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    # initialising the elif condition based on user's choice for appending the tasks into the to-do list
    elif user_choice==4:
        new_task=input("Enter the name of the task to append: ")
        task.append(new_task)
        print("Task added successfully.")
    # initialising the elif condition based on user's choice for removing the tasks from the to-do list
    elif user_choice==5:
        for i, t in enumerate(task, 1):
            print(f"{i}. {t}")
        remove_task_num=int(input("Enter the number of the task to be removed: ")) - 1
        if 0<=remove_task_num<len(task):
            removed_task=task.pop(remove_task_num)
            print(f"{removed_task} has been successfully removed from your to-do list.")
        else:
            print("Invalid task number.")
    # initialising the if condition based on user's choice for closing the to-do list
    elif user_choice==6:
        print("closing your To-do List.")
        break
    else:
        print("Invalid Choice\n")
        break
