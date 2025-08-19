A,B,C = map(int, input().split())

if B<C:
    n = A//(C-B)+1
    print(n)
else:
    print(-1)