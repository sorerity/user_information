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
    if retry == "N":
        break

file = open("personal_information.txt", "w")
for persons__order, user_list in enumerate (personal_info, start=1):
    file.write(f"Person {persons__order}:\n")
    for field_name, field_value in user_list.items():
        file.write(f"{field_name}: {field_value}\n")
    file.write("\n")