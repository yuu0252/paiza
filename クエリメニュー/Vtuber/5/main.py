from collections import defaultdict

N = int(input())

superchat = defaultdict(int)
members = []

for _ in range(N):
  s = input().split()
  if s[1] == "give":
    superchat[s[0]] += int(s[2])
  else:
    members.append(s[0])

for name, price in sorted(superchat.items(), key=lambda x:(x[1], x[0]), reverse=True):
  print(name)

for name in sorted(members):
  print(name)