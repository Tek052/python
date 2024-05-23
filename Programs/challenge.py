name = input("Enter your name")
age = int(input("Enter your age"))

#if 18 <= age < 31:  same way for write the code
if age >= 18 and age < 31:
    print("Welcome to the holiday club {}".format(name))
else:
    print("Your are not allow to go in holiday")