n, t = map(int, input().split())
k = int(input())
S = map(int, input().split())

count = 0

ad_list = {}

for i in range(1, n+1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

for i in S:
    for j in ad_list[i]:
        ad_list[j].remove(i)
    ad_list[i].clear()

def dfs(v, path):
    for i in ad_list[v]:
        if i not in path:
            path.append(i)
            dfs(i, path)
            path.pop()
        elif i == t and len(path) > 2:
            path.append(i)
            global count
            count += 1
            path.pop()

dfs(t, [t])

print(count // 2)