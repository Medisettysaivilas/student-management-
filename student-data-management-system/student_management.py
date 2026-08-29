import json
import os

FILE_NAME = "students.json"


# Load students from JSON file
def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


# Save students to JSON file
def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


# Add a new student
def add_student(students):
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ").strip()

    # Check duplicate ID
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ").strip()

    while True:
        try:
            age = int(input("Enter Age: "))
            if age <= 0:
                print("Age must be greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a valid age.")

    course = input("Enter Course: ").strip()
    grade = input("Enter Grade: ").strip()

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "grade": grade
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


# Display all students
def display_students(students):
    print("\n--- All Students ---")

    if not students:
        print("No students found.")
        return

    for student in students:
        print("----------------------------")
        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Age        :", student["age"])
        print("Course     :", student["course"])
        print("Grade      :", student["grade"])


# Search student
def search_student(students):
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("----------------------------")
            print("Student ID :", student["id"])
            print("Name       :", student["name"])
            print("Age        :", student["age"])
            print("Course     :", student["course"])
            print("Grade      :", student["grade"])
            return

    print("Student not found.")


# Update student
def update_student(students):
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID: ").strip()

    for student in students:
        if student["id"] == student_id:

            print("Leave a field empty if you don't want to change it.")

            name = input(f"Name [{student['name']}]: ").strip()
            age = input(f"Age [{student['age']}]: ").strip()
            course = input(f"Course [{student['course']}]: ").strip()
            grade = input(f"Grade [{student['grade']}]: ").strip()

            if name:
                student["name"] = name

            if age:
                try:
                    student["age"] = int(age)
                except ValueError:
                    print("Invalid age. Old age kept.")

            if course:
                student["course"] = course

            if grade:
                student["grade"] = grade

            save_students(students)

            print("Student updated successfully!")
            return

    print("Student not found.")


# Delete student
def delete_student(students):
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ").strip()

    for student in students:
        if student["id"] == student_id:

            confirm = input(
                f"Are you sure you want to delete {student['name']}? (y/n): "
            ).lower()

            if confirm == "y":
                students.remove(student)
                save_students(students)
                print("Student deleted successfully!")
            else:
                print("Delete cancelled.")

            return

    print("Student not found.")


# Main menu
def main():
    students = load_students()

    while True:
        print("\n================================")
        print("   STUDENT DATA MANAGEMENT")
        print("================================")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("\nThank you for using Student Data Management System!")
            break

        else:
            print("Invalid choice. Please select 1-6.")


# Start program
if __name__ == "__main__":
    main()