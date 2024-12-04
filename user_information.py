print("Personal Information:")

while True:

    while True:
        name = input("Name: ")
        if name.isalpha():
            break
        else:
            print("Error, please enter letters only.")
        
    while True:
        age = input("Age: ")
        if age.isdigit():
            break
        else:
            print("Error, Age should contain numbers only.")
    
    while True:
        try:
            int(input("Number: "))
            break
        except:
            print("Error, Please enter numbers only.")
    



































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