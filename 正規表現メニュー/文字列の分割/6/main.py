import re

s = input()

s = re.sub(r'import [a-zA-Z0-9]', '', s)

print(s)