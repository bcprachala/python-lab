# Write your code here :-)
import re
p=re.compile('\d{3}[-|\.|\s]\d{3}[-|\.|\s]\d{4}')
r=p.findall('3345-766-907 ,886-245-9772')
print(r)

a=re.compile('\w+\d+\w*@gmail\.com')
t=a.findall(' hsn2002@gmail.com,abc.in,adef2008@gmail.com')
print(t)
