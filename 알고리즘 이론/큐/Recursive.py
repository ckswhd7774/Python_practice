# 재귀 Recursive
def DFS(n):
    if n == 0:
        return 
    else :
        print(n, end='')
        DFS(n-1)
        
DFS(3)

# 피보나치(재귀)
def fibo(n):
    if n <= 2 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)
    
fibo(35)

# memoization(메모리 제이션)
def fibo2(n):
    if dy[n] > 0 :
        return dy[n]
    if n <= 2 :
        return 1
    else :
        dy[n] = fibo(n-1) + fibo(n-2)
        return dy[n]
dy = [0] * 50
fibo2(40)