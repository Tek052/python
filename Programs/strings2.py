#                   1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:9]) #Norwegian
print(parrot[-14:-5])#Norwegian

print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

number = "9,223;372:036 854,775;807"
seperators = number[1::4] ## Print from 1 to the end in step by 4
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
