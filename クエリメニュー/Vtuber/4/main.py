from collections import defaultdict

departments = defaultdict(list)

N, K = map(int, input().split())

S = [input() for _ in range(N)]

for _ in range(K):
  a, p, m = input().split()
  m = int(m)

  departments[a].append((p, m))

for s in S:
  print(s)
  for p, m in departments[s]:
    print(p, m)
  print("-----")