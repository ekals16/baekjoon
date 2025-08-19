day = int(input())
c1,c2,c3,c4,c5 = map(int, input().split())
n=0

if day==c1:
    n = n+1
if day==c2:
    n = n+1
if day==c3:
    n = n+1
if day==c4:
    n = n+1
if day==c5:
    n = n+1

print(n)