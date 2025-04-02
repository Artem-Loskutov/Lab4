def longestIncreasingSubsequence(arr):
    n = len(arr)
    dp = [1] * n
    prevElementIndex = [-1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prevElementIndex[i] = j

    length = max(dp)
    lastElementIndex = dp.index(length)
    lis = []

    while lastElementIndex != -1:
        lis.append(arr[lastElementIndex])
        lastElementIndex = prevElementIndex[lastElementIndex]

    lis.reverse()
    return length, lis


with open("input.txt", "r") as f:
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().split()))

length, subseq = longestIncreasingSubsequence(arr)

with open("output.txt", "w") as f:
    f.write(f"{length}\n")
    f.write(" ".join(map(str, subseq)) + "\n")