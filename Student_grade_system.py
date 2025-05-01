Student_grades = { }

def add_student(name,grade):
    Student_grades[name] = grade
    print(f"added {name} with a {grade}")
    
def update_student(name,grade):
    if name in Student_grades:
        Student_grades[name] = grade
        print(f"{name} with marks are update {grade}")
    else:
        print(f"{name} is not found!")
    
def delete_student(name):
    if name in Student_grades:
        del Student_grades[name]
        print(f"{name} has been successfully deleted!")
    else:
        print(f"{name} is not found!")
        
def disply_all_student():
    if Student_grades:
        for name, grade in Student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No students found/added")
        
def main():
    while True:
        print("\n Student Grades Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")
        
        choice = int(input("Enter your choice ? = "))
        if choice == 1 :
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            add_student(name,grade)
            
        elif choice == 2 :
            name = input("Enter the student name = ")
            grade = int(input("Enter student grade = "))
            
            update_student(name,grade)
            
        elif choice == 3 :
            name = input("Enter student name = ")
            delete_student(name)
            
        elif choice == 4 :
            disply_all_student()
            
        elif choice == 5 :
            print("Closing the program...")
            break
        else:
            print("Invalid choice!")
            
main()






