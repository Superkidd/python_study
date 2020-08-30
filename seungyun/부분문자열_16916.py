# 런타임 오류 발생
import sys
full_string, part_string = sys.stdin.readline().split()
print(int(part_string in full_string))
