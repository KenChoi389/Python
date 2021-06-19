from collections import deque
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ') #한칸씩 띄워 한줄에 출력
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


visited=[False]*9
dfs(graph,1,visited)

def bfs(graph,start,visited2):
    queue=deque([start])
    visited2[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i]=True


visited2=[False]*9
bfs(graph,1,visited)