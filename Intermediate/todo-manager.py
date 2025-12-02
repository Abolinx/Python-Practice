class Task:
    def __init__(self, name, description, priority, due_date = None, state = "pending⌛"):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.state = state

def add_task():
    pass

def view_tasks():
    pass

def mark_as_complete():
    pass

def delete_task():
    pass

def main():
    while True:    
        print("\n-----# Todo-Manager Menu #-----\n")
        print("(A) -> add task \n(V) -> view tasks \n(C) -> mark as complete \n(D) -> delete task \n(Q) -> exit \n")
        user_input = input("Please enter what you want to do?(A, V, C, D, Q)?:")

        if user_input == "A":
            add_task()
            continue

        elif user_input == "V":
            view_tasks()
            continue

        elif user_input == "C":
            mark_as_complete()
            continue

        elif user_input == "D":
            delete_task()
            continue

        elif user_input == "Q":
            print("Bye Bye👋")
            break

        else:
            print("Invalid input! Assumed exit.")
            break

if __name__ == "__main__":
    main()