name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
year_born = input("Enter the year you were born: ")

print("Registration Form")
print()
print("First name: ", name)
print("Last name: ", last_name)
print("Birth date: ", year_born)
print()
print("Welcome ", name, last_name,"!")
print("Your registration is complete.")
print("Your temporary password is: ", name + "*" + year_born)


