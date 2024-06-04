from collections import defaultdict

n, m, s = map(int, input().split())

ad_list = defaultdict(list)

for _ in range(m):
  a, b = map(int, input().split())
  ad_list[a].append(b)

if len(ad_list[s]) > 0:
  print(*sorted(ad_list[s]))
else:
  print(-1)