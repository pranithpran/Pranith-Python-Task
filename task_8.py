# Student Management System using Dictionary and Set

students = {}  # dictionary to store student data


def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    course_count = int(input("How many courses? "))

    courses = set()  # using set to store unique courses
    for _ in range(course_count):
        course = input("Enter course name: ")
        courses.add(course)

    students[roll] = {
        "name": name,
        "courses": courses
    }

    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No students found!\n")
        return

    for roll, info in students.items():
        print(f"Roll No.: {roll}")
        print(f"Name: {info['name']}")
        print(f"Courses: {', '.join(info['courses'])}")
        print("-" * 30)


def search_student():
    roll = input("Enter roll number to search: ")
    if roll in students:
        info = students[roll]
        print(f"Name: {info['name']}")
        print(f"Courses: {', '.join(info['courses'])}")
    else:
        print("Student not found!")


# ---------------- Main Menu ------------------

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Try again.\n")