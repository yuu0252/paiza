n = int(input())
ad_list = {}

for i in range(1, n+1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

def dfs(v, connected_comp):
    for i in ad_list[v]:
        if i not in connected_comp:
            connected_comp.append(i)
            dfs(i, connected_comp)
    return connected_comp

cnt = 0
not_visit = set(range(1, n+1))
while len(not_visit) > 0:
    v = not_visit.pop()
    not_visit -= set(dfs(v, [v]))
    cnt += 1

print(cnt)