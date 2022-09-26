a = [9, 4, 1, 7, 6, 8, 3, 5, 2]
cnt = 0


def straight_insertion_sort(a):
    global cnt
    n = len(a)
    h = n//2
    while h > 0:
        for i in range(h, n):  # i=1~6
            temp = a[i]
            j = i-h
            while j >= 0 and a[j] > temp:  # temp보다 왼쪽값이 크다면
                a[j+h] = a[j]  # a[j]위치에 덮어쓰기!
                j -= h
                cnt += 1
            a[j+h] = temp  # 마지막으로 덮어쓴 j 왼쪽값(j-=1)에 최종적으로 temp 덮어쓰기
        h//=2


straight_insertion_sort(a)
print(a)
# print(cnt)
