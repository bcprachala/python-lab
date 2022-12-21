# Write your code here :-)
import re
def isphoneno(s):
    Pattern=re.compile("\d{3}-\d{3}-\d{4}")
    return Pattern.match(s)
s="415-353-2544"
if(isphoneno(s)):
    print("valid no")
else:
    print("invalid")
