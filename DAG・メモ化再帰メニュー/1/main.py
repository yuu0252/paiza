import sys
import threading

# 再帰回数上限値のセット。引数にはPythonインタープリタのスタックの深さを指定する
sys.setrecursionlimit(67108864)
#　2^20のstackメモリを確保
threading.stack_size(1024*1024)

def fib(n, memo={}):
  if n in memo:
    return memo[n]
  if n == 0:
    memo[0] = 0
  elif n == 1:
    memo[1] = 1
  else:
    memo[n] = (fib(n - 1, memo) + fib(n - 2, memo)) % 1000000007
  return memo[n]

if __name__ == "__main__":
  n = int(input())
  print(fib(n))