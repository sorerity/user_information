print("Personal Information:")

personal_info = []

while True:

    while True:
        name = input("Name: ")
        if name.isalpha():
            break
        else:
            print("Error, Please enter letters only.")
        
    while True:
        try:
            age = int(input("Age: "))
            break
        except:
            print("Error, please enter valid age.")

    while True:
        number = input("Number: ")
        if number.isdigit() and len(number) == 11:
            break
        else:
            print("Error, please input a valid number.")
                
    while True:
        address = input("Address: ")
        break
    
    while True:
        try:
            zipcode = int(input("Zip Code: "))
            break
        except:
            print("Error, please enter numbers only.")

    user_list = {
        "Name" : name,
        "Age" : age,
        "Number" : number,
        "Address" : address,
        "Zip Code" : zipcode,
    }
    personal_info.append(user_list)

    while True:
        retry = input("Would you like to input another entry? Y/N: ")
        if retry == "Y":
            break
        elif retry == "N":
            break

    file = open("personal_information.txt", "w")
    for user_list in personal_info:
        for key, value in user_list.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")
































#Create a program that ask user for personal information. 
#Minimum of 5 information per person, more info the better. eg. Fullname, Address, etc. 
#Write the collected information in a txt file. It's up to you on how you'd like to format the information in the file. 
#The program should ask user if want to input another person or exit.

#print Personal Information

#establish a while true loop
    #ask user to input
        #Name
        #Age
        #Contact Num.
       # Address
       # Zip Code 
   # append each answer to the dict
   # add a dict
#ask the user if they still want to add another person
#if Y, loop back to the while true loop
#if N, BREAK

#open a .txt file 
#for each person in dict
    #write each info

#file handle close