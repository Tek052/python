age = int(input("How old are you"))

#if age >= 16 and age <= 65: same code
#if 16 <= age <= 65:  #different way to write our code
if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")
    
print("-" * 80)

if age < 16 or age > 65:

    print("Have a good day at work")
else:
    print("Enjoy your free time")
