# This program inputs the number of students registering and reads that many student IDs
# Adds StudentId captured from user and the dotted lines after each student for them to sign during 
# registration in file reg_form.txt

no_of_students = int(input("How many students are registering? : ")) # Get number of students from user

with open("reg_form.txt","w") as file: # Open file reg_form.txt for write mode
    file.write("STUDENT ID\t") # Write header STUDENT ID
    file.write("SIGNATURE\n\n") # Write header SIGNATURE

    for i in range(no_of_students): # Loop through from 0 to no_of_students 

        student_id = input(f"Enter Student ID {i+1}: ") # Get student_id from user

        file.write(student_id+"\t\t") # Write the student id into the file and append a tab after it

        file.write("-----------------------"+"\n") # Write dotted lines to the file and append a newline

# file is not closed as used with open as sytanx for file opening