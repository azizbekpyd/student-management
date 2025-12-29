import json
FILENAME = "students_data.json"
students = {}
current_id_counter = 1

def get_id(name):
    for key, st in students.items():
        if st['name'].lower() == name.lower():
            return key
    return None

def load_data():
    global current_id_counter, students
    try:
        with open(FILENAME, 'r') as file:
            students = json.load(file)
            if students:
                last_id = max(int(key) for key in students.keys())
                current_id_counter = last_id + 1
    except FileNotFoundError:
        students = {}
        
def save_data():
    with open(FILENAME, 'w') as file:
        json.dump(students, file, indent=4)
    print("The data is successfully saved!")

def save_and_print(message):
    save_data()
    print(message)

def pause():
    input("\nPress Enter to continue...")

load_data()

def get_valid_score():
    while True:
        try:
            score = int(input("Score: "))
            if 0<= score <= 100:
                return score
            print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_student():
    global current_id_counter
    name = input("Name: ") 
    while not name:
        name = input("Name cannot be empty. Enter name: ") 
    
    if get_id(name):
        print(f"Error: A student named {name} already exists.")
        return

    score = get_valid_score()
    clean_name = name.strip().title()
    new_student = {'name': clean_name, 'score': score} 
    students[str(current_id_counter)] = new_student
    save_and_print(f"Student added with ID: {current_id_counter}")
    current_id_counter += 1
        
def update_student():
    name = input("Which student's score do you want to change? Name: ")
    student_id = get_id(name)
    if student_id:
        new_score = get_valid_score()
        students[student_id]['score'] = new_score
        save_and_print(f"{name}'s score is now updated!")
    else:
        print("There is no student with this name!")

def delete_student():
    name = input("Which student do you want to delete? Name: ")
    student_id = get_id(name)
    if student_id:
        del students[student_id]
        save_and_print(f"Student {name} with the ID of {student_id} is deleted!")
    else:
        print("There is no student with this name!")

def show_students():
    if students:
        print("-"*30)
        print(f"Id   |   Name   | Score  |   Status")
        for key in sorted(students, key = int):
            value = students[key]
            status = "Passed" if value['score'] >= 60 else "Failed"
            print(f"{key:<5}| {value['name']:<10}| {value['score']:<5}| {status}")
        print("-"*30)
    else:
        print("The student list is currently empty!")
        
def show_statistics():
    if students:
        scores = [val['score'] for val in students.values()]
        passed_students = sum(1 for st in students.values() if st['score'] >= 60)
        max_score = max(scores)
        min_score = min(scores)
        avg_score = sum(scores)/len(scores)
        print(f"\nPassed students: {passed_students}\nMax score: {max_score}\nMin score: {min_score}\nAverage score: {avg_score:.2f}")
    else:
        print("There is no data!")

while True:
    print(
        '''
        1. Add student
        2. Update student score
        3. Delete student
        4. Show all students
        5. Show statistics
        6. Exit
        '''
        )
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        add_student()
        pause()
    elif choice == '2':
        update_student()
        pause()
    elif choice == '3':
        delete_student()
        pause()
    elif choice == '4':
        show_students()
        pause()
    elif choice == '5':
        show_statistics()
        pause()
    elif choice == '6':
        print('Exiting...\nGoodbye!')
        break
    else:
        print('Invalid choice!')
        pause()