"""
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
"""
num = int(input())

a = input().split()
max = int(a[0])
min = int(a[0])

for j in range(len(a)):
    if max < int(a[j]):
        max = int(a[j])
    if min > int(a[j]):
        min = int(a[j])
print(min,max)