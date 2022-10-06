import sys
input=sys.stdin.readline

n=int(input())
a=list(list(map(int,input().split())) for _ in range(n))

white,blue=0,0

def div(x,y,n):
    global white,blue
    color =a[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if a[i][j]!=color:
                half=n//2
                div(x,y,half)
                div(x,y+half,half)
                div(x+half,y,half)
                div(x+half,y+half,half)
                return
    if color==0:
        white+=1
    else:
        blue+=1


div(0,0,n)
print(white)
print(blue)