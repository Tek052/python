         # 01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

Backwards = letters[25:0:-1] ##zyxwvutsrqponmlkjihgfedcba
backwards = letters[::-1] ##zyxwvutsrqponmlkjihgfedcb
print(backwards)
print(Backwards)

print(letters[16:13:-1])#qpo
print(letters[4::-1])#edcba
print(letters[:18:-1])#zyxwvut

print(letters[-4:])#wxyz
print(letters[-1:])#z
print(letters[:1])#a
print(letters[0])#a