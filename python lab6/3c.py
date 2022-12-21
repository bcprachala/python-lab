# Write your code here :-)
def has_duplicates(list1):

     for i in list1:
         s=list1.count(list1[i])
         if(s>1):
             print("true")
             break

has_duplicates([1,2,3,3,5])
