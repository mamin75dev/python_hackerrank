n = int(input())
arr = map(int, input().split())
arr = list(arr)
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[j] > arr[i]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

for i in range(len(arr)):
    if (arr[i+1] != arr[i]):
        print(arr[i+1])
        break