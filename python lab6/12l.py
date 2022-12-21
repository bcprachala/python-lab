# Write your code here :-)
mylist = ["apple", "orange", "cherry"]

x = len(mylist)

print(x)


txt = ",,,,,rrttgg.....fruit....rrr"

y = txt.strip(",.grt")

print(y)


string = "goatssss"
print(string.rstrip('s'))

string = "goatssss"
print(string.lstrip('s'))


txt = "Hello, welcome to my world."

z = txt.find("welcome")

print(z)


txt = "hi welcome, hey welcome."

a = txt.rfind("welcome")

print(a)


string = " this is bat and ball"
v=string.index('bat')
print(v)


txt = "Hello, welcome to my world."
c = txt.rindex("e")
print(c)


fruits = ["apple", "cherry", "cherry"]

d= fruits.count("cherry")

print(d)

txt = "welcome to the python lab"
e = txt.split()
print(e)


txt = "I like bananas"

e = txt.replace("bananas", "apples")

print(e)


text = ['Python', 'programming', 'language']
print(' '.join(text))


txt = "Hello my friends"
f = txt.upper()
print(f)

txt = "Hello my friends"
g = txt.lower()
print(g)

txt = "Hello its pyhton"
h = txt.swapcase()
print(h)

txt="Python Programming Language"
i=txt.istitle()
print(i)

j=txt.capitalize()
print(j)


txt = "Hello, welcome to my world."
k = txt.startswith("Hello")
print(k)

l=txt.endswith("hello")
print(l)
