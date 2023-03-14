with open('input.txt', 'r') as f:
    l, n = map(int, f.readline().split())
    x = list(map(int, f.readline().split()))
    x.append(l)
    x = [0] + x


dp = [[0] * (len(x)) for _ in range(len(x))]
for i in range(2, len(dp)):
    for j in range(0, len(dp)-i):
        l, r = j, j+i
        min_ = 10**7
        for k in range(l+1, r):
            if dp[l][k] + dp[k][r] < min_:
                min_ = dp[l][k] + dp[k][r]
        dp[l][r] = x[r] - x[l] + min_

print(dp[0][-1])
