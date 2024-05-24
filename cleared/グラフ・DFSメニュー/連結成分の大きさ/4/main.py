n, k = map(int, input().split())
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

not_visited = set(range(1, n+1))

while len(not_visited) > 0:
    v = not_visited.pop()
    res = dfs(v, [v])
    if len(res) > k:
        print("No")
        exit()
    not_visited -= set(res)

print("Yes")