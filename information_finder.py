with open("personal_information.txt", "r") as personal_info:
    file_lines = personal_info.readlines()

search_name = input("Enter the name that you want to search: ")

name_found = False

for line_index, file_line in enumerate(file_lines):
    if search_name in file_line:
        name_found = True
        print("Information Found: ")
        
        for line_offset in range(5):
            print(file_lines[line_index + line_offset].strip())
        break

if not name_found:
    print("Error, Name is not in the file.")

























#Create another program that ask user for fullname.
#Find the full name in the txt file (output of program1). 
#Display the informations found in the txt file.

#Open the .txt file in read mode
#read all the lines from the file

#Ask user for the name they want to search for
#Read all lines from the File 
#Search for the name in the File
    #if found, display information
    #if not found, display "Name not found."

#Close File
#end