import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(v, group):
    visited[v] = group
    for i in graph[v]:
        if visited[i] == 0:
            temp = dfs(i, -group)
            if not temp:
                return False
        elif visited[i] == group:
            return False
    return True

n = int(input())
for _ in range(n):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0]*(v+1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for start in range(1,v+1):
        if not visited[start]:
            check= dfs(start, 1)
            if not check:break
    print("YES" if check else "NO")