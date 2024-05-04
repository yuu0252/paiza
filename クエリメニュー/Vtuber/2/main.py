N, K = map(int, input().split())
members = [None] * K

for i in range(N):
  input()

for i in range(K):
  year, name = input().split()
  members[i] = (int(year), name)

for year, name in sorted(members):
  print(name)