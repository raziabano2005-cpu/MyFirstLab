# Student Management System - Lab 2

students = []

def add_student():
    name = input("Student Name: ")
    roll = input("Roll No: ")
    students.append({"name": name, "roll": roll})
    print("Student Added!")

def show_students():
    print("\n--- Student List ---")
    for s in students:
        print(f"Name: {s['name']}, Roll No: {s['roll']}")

# Main
while True:
    print("\n1. Add Student \n2. Show Students \n3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")