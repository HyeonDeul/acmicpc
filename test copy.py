from itertools import combinations
import random

arr = [
    '조아름',
    '최주향',
    '김다인',
    '이지민',
    '고도혁',
    '정덕현',
    '최명진',
    '이수빈',
    '이효진',
    '전현수',
    '김아영',
    '김열국',
    '이민우',
    '최지우',
    '문예원',
    '김대원',
    '심준혁',
    '주재연',
    '홍지승',
    '김시온',
    '김영희',
    '송은지',
    '김택정',
    '전서영',
    '김이새',
    '정지원',
    '김원교',
    '김인호',
    '김찬미',
    '김주희',
    '김서현',
    '김미래',
    '김인애',
    '전하영',
    '김정은',
    '이효리',
    '이아현',
    '조나영',
]

print(len(arr))
random.shuffle(arr)
ans = []
with open('jo.txt', 'w', encoding='utf-8') as f:
    while len(arr) >= 2:
        result = list(combinations(arr, 2))[0]
        print(result)
        ans.append(list(result))
        for i in result:
            arr.remove(i)

    line = """"""
    for i in ans:
        line += ', '.join(i)+'\n'
    f.write(line)
