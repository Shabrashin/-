from collections import deque


with open('input.txt', 'r') as f:
    n, k = map(int, f.readline().split())
    arr = list(map(int, f.readline().split()))


d = deque()
d.append(arr[0])
for i in range(1, k):
    while len(d) != 0 and d[-1] > arr[i]:
        d.pop()
    d.append(arr[i])

for i in range(k, n):
    print(d[0])
    # new
    if arr[i-k] == d[0]:
        d.popleft()
    while len(d) != 0 and d[-1] > arr[i]:
        d.pop()
    d.append(arr[i])

print(d[0])
