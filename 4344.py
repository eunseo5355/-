"""
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다.
당신은 그들에게 슬픈 진실을 알려줘야 한다
"""
num = int(input())
for i in range(num):
    a = input().split()
    sum = 0
    for x in range(1, len(a)):
        sum += int(a[x])
    ava = sum / int(a[0])
    count = 0
    for y in range(1, len(a)):
        if int(a[y]) > ava:
            count += 1
    v = count/int(a[0])*100
    print("%.3f%%" % (round(v, 3)))
