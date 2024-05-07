import re

s = input()

s = re.search(r'G\D?C??', s)
print(s.start())