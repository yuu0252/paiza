import re

s = input()
s = re.split(r'-.{3,}', s)

for i in s:
  print(i)