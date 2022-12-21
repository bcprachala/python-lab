# Write your code here :-)
def middle(t):
    t.pop(-1)
    t.pop(0)
    return t
t=[1,2,3,4,5]
print(middle(t))
