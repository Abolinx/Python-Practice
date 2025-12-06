user_tasks = []

class Task:
    def __init__(self, name, description, priority, due_date, state):
        self.name = name
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.state = state
    
    
def add_task():
    '''
    - get task name 
    - append to task list 
    - get description 
    - get priority
    - get due date
    - get state  

    '''
    new_task = Task(input("Please enter name of your task:"), input("Please enter description:"), int(input("Please enter priority(1-7):")), input("Please enter due date (Ex: 1hour):"), input("Please enter state (default:pending):"))
    user_tasks.append(new_task)

def view_tasks_S():
    view_list = []
    for task in user_tasks:
        if task.state.lower() == "pending":
            view_list.append(task)
    return view_list

def view_tasks_P():
    view_list = user_tasks
    for i in range(0, len(view_list)-1):
        for j in range(len(view_list)-1):
            if view_list[j].priority > view_list[j+1].priority:
                view_list[j+1] , view_list[j] = view_list[j] , view_list[j+1] 
    return view_list

def print_view_tasks(list):
            
        print("\n------# view of tasks #-------\n")
        for index, task in enumerate(list):
            print(f"{index + 1}.{task.name}:{task.description}-->>{task.state} with {task.priority}th priority")
            print("--------------------------------------------------")

def view_tasks():
    '''
    Docstring for view_tasks
    '''

    Filter_or_No = input("Do you want to filter tasks?(yes/no):")

    if Filter_or_No.strip().lower() == "yes":
        filter_type = input("state(+) or Priority(-)?:")
    
        if filter_type == "+":
           view_list = view_tasks_S()
        
        elif filter_type == "-":
            view_list = view_tasks_P()
        
        else:
            print("Invalid input!")
            return ""
        
        print_view_tasks(view_list)

    elif Filter_or_No.strip().lower() == "no":
        print_view_tasks(user_tasks)

    else:
        print("Invalid input!")
        return ""
        

def mark_as_complete():
    '''
    Docstring for mark_as_complete
    '''
    view_list = []
    while True:
        mark = input("do you want marking some tasks?(yes/no):")
        if mark.strip().lower() == "yes":
            for task in user_tasks:
                if task.state.lower() == "pending":
                    view_list.append(task)
            print("\n------# view of tasks #-------\n")
            for index, task in enumerate(view_list):
                    print(f"{index + 1}.{task.name}:{task.description}-->>{task.state} and {task.priority}")
                    print("--------------------------------------------------")
            
            task_index = int(input("Which task do you want to mark?"))
            view_list[task_index-1].state = "completed"
            print(f"The your task ({view_list[task_index-1].name}) is {view_list[task_index-1].state}.")
        else:
            print("Maybe there are still tasks to complete.")
            return ""

def delete_task():

    print_view_tasks(user_tasks)
    task_index_4_del = int(input("witch task you want delete it?"))
    deleted_task = user_tasks.pop(task_index_4_del-1)
    print(f"{delete_task.name} is deleted!")

def main():
    while True:    
        print("\n-----# Todo-Manager Menu #-----\n")
        print("(1).add task \n(2).view tasks \n(3).mark as complete \n(4).delete task \n(0).exit \n")
        user_input = input("Please enter what you want to do?(1-4 or 0)?:")

        if user_input == "1":
            add_task()
            continue

        elif user_input == "2":
            view_tasks()
            continue

        elif user_input == "3":
            mark_as_complete()
            continue

        elif user_input == "4":
            delete_task()
            continue

        elif user_input == "0":
            print("Bye Bye👋")
            break

        else:
            print("Invalid input! Assumed exit.")
            break

if __name__ == "__main__":
    main()