def binary_search(A, n, k):
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == k:
            return True
        if A[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

n = int(input())
A = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    k = int(input())
    if binary_search(A, n, k):
        print("Yes")
    else:
        print("No")