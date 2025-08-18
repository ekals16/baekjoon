N,M = map(int, input().split())
if ( N,M>=0 or N,M<=0 ) and N<M:
    print(M-N)
else:
    print(N-M)