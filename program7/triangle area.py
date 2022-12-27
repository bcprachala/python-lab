# Write your code here :-)
def triangle(a,b,c):
    if a + b >= c and b + c >= a and c + a >= b :
        return True

    else:
        return False

a = float(input('Enter length of side a: '))

b=float(input('Enter length of side b: '))
c= float(input('Enter length of side c: '))

if triangle(a,b,c):
    print('Triangle is Valid.')
    s = (a+b+c) / 2
    area = (s* (s-a)*(s-b) * (s-c))** 0.5
    print('The area of the triangle is', area)
else:
    print('Triangle is Invalid.')
