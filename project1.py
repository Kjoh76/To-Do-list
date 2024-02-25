def create_task():
    pass

def delete_task():
    pass

def view_task_list():
    pass

def view_completed():
    pass

def mark_complete():
    pass

def load_from_file():
    pass

def write_to_file():
    pass

def menu_display():
    print('1: Create a Task')
    print('2: Delete a Task')
    print('3: View Task List')
    print('4: View Completed Task List')
    print('5: Mark a Task Completed')
    print('6: Load From a File:')
    print('7: Write to a File:')
    print('0: Quit')

while True:
    menu_display()
    user_choice = input("Enter your choice: ")
    if user_choice == '0':
        break
    elif user_choice == '1':
        create_task()
    elif user_choice == '2':
        delete_task()
    elif user_choice == '3':
        view_task_list()
    elif user_choice == '4':
        view_completed()
    elif user_choice == '5':
        mark_complete()
    elif user_choice == '6':
        load_from_file()                
    elif user_choice == '7':
        write_to_file()
    else:
        print('invalid choice')

