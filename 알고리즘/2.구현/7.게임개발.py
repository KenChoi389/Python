import sys
n,m=map(int,sys.stdin.readline().split())
x,y,dir=map(int,sys.stdin.readline().split())
data=[[]*m for _ in range(n)]
for i in range(n):
    data[i]=list(map(int,sys.stdin.readline().split())) #한 줄에 입력된 원소들을 리스트화 시켜줌
dx=[-1,0,1,0]
dy=[0,1,0,-1]



# print(data)
for i in range(n):
    for j in range(m):
        print(data[i][j],end=' ')
    print()