# Write your code here :-)
import re
def change_date(date):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
date = input('enter date')
print("Original date in YYY-MM-DD Format: ",date)
print("New date in DD-MM-YYYY Format: ",change_date(date))
