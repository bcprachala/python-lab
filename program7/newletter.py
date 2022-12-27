# Write your code here :-)
print("Enter a string of 4 characters: ")

string=input()
newstr=''

for i in string:
    ascii = ord(i)

    nextletter=chr(ascii+1)
    newstr=newstr+nextletter

print("Replaced string is", newstr)
