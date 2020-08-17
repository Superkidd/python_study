N = int(input())
number_in_card = list(map(int,input().split()))
M = int(input())
find_number = list(map(int,input().split()))
result =[]

number_in_card.sort() # 이분탐색 조건

for i in find_number: # 찾을값들 반복
    start = 0 # 배열의 첫 인덱스 값
    end = N-1 # 배열의 마지막 인덱스 값
    center = 0 # 이분탐색할 때 그 중간값 인덱스
    temp = 0
    while start <= end : #  값 찾을때까지 계속 돌리기
        center = (start + end) // 2
        if i == number_in_card[center] : # i를 찾았다면 중복값은?
            l = 1 
            r = 1
            while(center-l >= start): #왼쪽 탐색 
                if number_in_card[center-l] == number_in_card[center]:
                    l+=1
                else:
                    break
            while(center+r<= end): #오른쪽
                if number_in_card[center+r] == number_in_card[center]:
                    r+=1
                else:
                    break
            temp = l + r -1
            break
        elif i < number_in_card[center] : # 찾는값이 배열의 중간값보다 작으면 end를 center-1
            end = center - 1
        else : # 찾는값이 배열중간값보다 더 크면 start를 center+1
            start = center + 1

    result.append(temp) # temp 값 result에 저장
for i in result:
    print(i, end=' ')