import sys
input = sys.stdin.readline
N,M = map(int,input().split()) # A배열의 크기 = N , B배열의 크기 = M
result = list(map(int,input().split()))+list(map(int,input().split()))
print(' '.join(map(str, sorted(result))))