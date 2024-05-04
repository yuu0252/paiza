N, K = map(int, input().split())

bank = {}

for _ in range(N):
  name, p, d = input().split()
  bank[name] = (p, int(d))

for _ in range(K):
  g, m, w = input().split()
  p, d = bank[g]

  if p != m:
    continue

  bank[g] = (m, d - int(w))

for name, d in bank.items():
  print(name, d[1])