students_list = []
marks_list = []
total = 0

while True:

    print("\n===== STUDENT GRADE MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. View Grades")
    print("5. View Statistics")
    print("6. Pass/Fail Status")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # 1. Add Student
    if choice == "1":

        number_of_students = int(input("How many students do you want to add? "))

        for i in range(number_of_students):
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))

            students_list.append(name)
            marks_list.append(marks)
            total += marks

            print("Student added successfully!")

    # 2. View Students
    elif choice == "2":

        if len(students_list) == 0:
            print("No students added yet.")

        else:
            average = total / len(students_list)

            highest_marks = marks_list[0]
            highest_student = students_list[0]

            for i in range(len(students_list)):
                if marks_list[i] > highest_marks:
                    highest_marks = marks_list[i]
                    highest_student = students_list[i]

            print("\n--- Student Details ---")
            print("Students:", students_list)
            print("Marks:", marks_list)
            print("Total:", total)
            print("Average:", average)
            print("Highest scorer:", highest_student)
            print("Highest marks:", highest_marks)

    # 3. Search Student
    elif choice == "3":

        if len(students_list) == 0:
            print("No students added yet.")

        else:
            search = input("Enter student name to search: ")

            found = False

            for i in range(len(students_list)):
                if students_list[i] == search:
                    print(f"{students_list[i]} -> {marks_list[i]}")
                    found = True

            if not found:
                print("Student not found.")

    # 4. View Grades
    elif choice == "4":

        if len(students_list) == 0:
            print("No students added yet.")

        else:
            print("\n--- Grades ---")

            for i in range(len(students_list)):

                if marks_list[i] > 90:
                    print(f"{students_list[i]} -> Grade A")

                elif marks_list[i] > 80:
                    print(f"{students_list[i]} -> Grade B")

                else:
                    print(f"{students_list[i]} -> Grade C")

    # 5. View Statistics
    elif choice == "5":

        if len(students_list) == 0:
            print("No students added yet.")

        else:
            average = total / len(students_list)

            highest_marks = marks_list[0]
            highest_student = students_list[0]

            for i in range(len(students_list)):
                if marks_list[i] > highest_marks:
                    highest_marks = marks_list[i]
                    highest_student = students_list[i]

            pass_count = 0
            fail_count = 0

            for i in range(len(students_list)):

                if marks_list[i] >= 50:
                    pass_count += 1

                else:
                    fail_count += 1

            pass_percentage = (pass_count / len(students_list)) * 100
            fail_percentage = (fail_count / len(students_list)) * 100

            print("\n--- Class Statistics ---")
            print("Total marks:", total)
            print("Average:", average)
            print("Highest scorer:", highest_student)
            print("Highest marks:", highest_marks)
            print("Number of students passed:", pass_count)
            print("Number of students failed:", fail_count)
            print("Pass percentage:", pass_percentage, "%")
            print("Fail percentage:", fail_percentage, "%")

    # 6. Pass/Fail Status
    elif choice == "6":

        if len(students_list) == 0:
            print("No students added yet.")

        else:
            print("\n--- Pass / Fail Status ---")

            for i in range(len(students_list)):

                if marks_list[i] < 50:
                    print(
                        f"{students_list[i]} is fail due to marks: {marks_list[i]}"
                    )

                else:
                    print(
                        f"{students_list[i]} is pass because they got: {marks_list[i]}"
                    )

    # 7. Exit
    elif choice == "7":

        print("Exiting Student Grade Manager...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
