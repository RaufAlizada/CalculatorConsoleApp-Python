print(f"\t\t\tCalculator Console App")
print(f"\t\t\t\t1 - ADDITION\n\t\t\t\t2 - SUBTRACTION\n\t\t\t\t3 - MULTIPLICATION\n\t\t\t\t4 - DIVISION\n\t\t\t\t0 - EXIT")
check = True
while check:
    section = input("Select your what do you want? - ")
    if section == "0":
        break
    first_number = int(input("Enter your first number - "))
    second_number = int(input("Enter your second number - "))
    if section == "1":
        print(f"The Answer is '{first_number} + {second_number} = {first_number + second_number}'")
    elif section == "2":
        print(f"The Answer is '{first_number} - {second_number} = {first_number - second_number}'")
    elif section == "3":
        print(f"The Answer is '{first_number} * {second_number} = {first_number * second_number}'")
    elif section == "4":
        print(f"The Answer is '{first_number} / {second_number} = {first_number / second_number}'")