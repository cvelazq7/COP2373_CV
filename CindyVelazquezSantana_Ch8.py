import csv

def write_grades_to_csv():
    with open('grades.csv', mode='w',newline='') as csvfile:
        writer = csv.writer(csvfile)

        #writing header
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # Get the number of students from the user
        num_students = int(input("Enter the number of students: "))

        # Loop to input each student's data
        for _ in range(num_students):
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            try:
                exam1 = int(input("Enter grade for Exam 1: "))
                exam2 = int(input("Enter grade for Exam 2: "))
                exam3 = int(input("Enter grade for Exam 3: "))
            except ValueError:
                print("Please enter valid integer grades.")
                continue

            # Writing the student's data as a row
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("Data written to grades.csv successfully.")

    # Call the function to write data

write_grades_to_csv()
