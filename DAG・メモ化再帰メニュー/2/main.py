from collections import defaultdict
from functools import lru_cache

MOD = 1000000007

job_relation = defaultdict(list)

@lru_cache(None)

def job_seq_count(job):
  if not job_relation[job]:
    return 1
  count = 0
  for j in job_relation[job]:
    count += job_seq_count(j)
    count %= MOD
  return count

def main():
  n = int(input())
  k = int(input())
  for _ in range(k):
    j, w = map(int, input().split())
    j -= 1
    w -= 1
    job_relation[w].append(j)
  for i in range(n):
    job_relation[i].sort(reverse=True)
  print(job_seq_count(n-1))

if __name__ == "__main__":
  main()