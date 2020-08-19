import sys
input = sys.stdin.readline
N = int(input()) #N입력
# print(type(N))
input_paper = []
for i in range(N): # N개수만큼 N개의 정수로 행렬입력
    temp = list(map(int,input().split()))
    input_paper.append(temp)

print(len(input_paper))
one_cnt = 0
min_cnt = 0
zero_cnt = 0

def _alg(x,y,N):
    global one_cnt,min_cnt,zero_cnt
    check = input_paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if check!=input_paper[i][j]:
                for a in range(3):
                    for b in range(3):
                        _alg(x+N//3*a,y+N//3*b,N//3)
                return
    if check ==-1:
        min_cnt+=1
    elif check== 0:
        zero_cnt+=1
    elif check ==1:
        one_cnt+=1
_alg(0,0,N)
print(one_cnt)
print(min_cnt)
print(zero_cnt)