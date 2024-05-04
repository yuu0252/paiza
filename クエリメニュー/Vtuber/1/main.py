members = set()

N, K = map(int, input().split())

for _ in range(N):
  members.add(input())

for _ in range(K):
  q = input().split()

  if q[0] == "handshake":
    ans = list(members)
    ans.sort()
    for a in ans:
      print(a)
  elif q[0] == "join":
    members.add(q[1])
  else:
    members.remove(q[1])