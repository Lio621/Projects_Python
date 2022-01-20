import random as ran
import re
regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

url = input('Enter the URL : ')
def url_check(value):
    if(re.match(regex, value) is not None):
        return 1
    else:
        return 2

myChar1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
myChar2 = ('1', '2', '3', '4', '5') 
myChar3 = ('!', '@', '#', '$', '%')

valid = url_check(url)

if(valid == 1):
    str1 = ''
    str2 = ''
    str3 = ''
    for j in range(0, 4):
        ind1 = ran.randint(0, len(myChar1)-1)
        if(re.search(r"[a-z]",url)):
            str1 += myChar1[ind1]
    for k in range(0, 3):
        ind2 = ran.randint(0, len(myChar2)-1)
        if(re.search(r'[0-9]',url)):
            str2 += myChar2[ind2]
    for l in range(0, 4):
        ind3 = ran.randint(0, len(myChar3)-1)
        if(re.search(r'\d',url)):
            str3 += myChar3[ind3]
    new_string = str1+str2+str3
else:
    print('Invalid URL!')

print('The new string is = ', new_string)