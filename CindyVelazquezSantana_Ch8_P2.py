import csv


# Function to read and display the data from grades.csv
def display_grades_from_csv():
    try:
        # Open the grades.csv file to read
        with open('grades.csv', mode='r') as file:
            reader = csv.reader(file)

            # Read the header
            header = next(reader)
            # Print the header in tabular format
            print(f"{header[0]:<15}{header[1]:<15}{header[2]:<10}{header[3]:<10}{header[4]:<10}")
            print("-" * 60)

            # Read and print each student's data
            for row in reader:
                print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")
    except FileNotFoundError:
        print("The file grades.csv does not exist. Please make sure it has been created.")


# Call the function to display data
display_grades_from_csv()