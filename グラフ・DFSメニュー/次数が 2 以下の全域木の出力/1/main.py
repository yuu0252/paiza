n = int(input())
ad_list = {}
edge_num = 0

for i in range(1, n+1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))
    edge_num += v

def dfs(v, path):
    for i in ad_list[v]:
        if i not in path:
            path.append(i)
            dfs(i, path)
    return path

if edge_num//2 > n-1:
    print("No")
else:
    if len(dfs(1, [1])) == n:
        print("Yes")
    else:
        print("No")