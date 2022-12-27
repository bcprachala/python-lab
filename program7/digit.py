# Write your code here :-)
print ('prime prime Enter a 4-digit number :')
num =int( input())

s = str(num)
sum=0
for i in s:
    print(i)

while(num>0):
    dig=num%10

    sum=sum+dig

    num=num//10

print("The sum of digits is :",sum)

