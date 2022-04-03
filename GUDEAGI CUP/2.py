answer = '0'
n = int(input())

for i in range(1, n+1):
    answer += bin(i).lstrip('0b')
print(answer)
