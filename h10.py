#KKO IT20
#Ülesanne 10
#09.12.2020
import re

fh = open('deez.txt')
for line in fh:
    if re.search(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",line):
         print(line,end='') 