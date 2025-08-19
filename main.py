A,B = map(int, input().split())
C = int(input())
total_minute = A*60 + B + C  

print((total_minute//60)%24, total_minute%60)