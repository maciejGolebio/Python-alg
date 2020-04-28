def next_smaller(n):
    flag = False
    ns = ''
    arr = list(reversed(str(n)))
    j = 0
    for i in range(len(arr)):
        if flag:
            break
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                flag = True
                break
    x = j
    for i in range(x):
        for j in range(i, x):
            if int(arr[i]) > int(arr[j]):
                arr[i], arr[j] = arr[j], arr[i]

    if not flag or arr[-1] == '0':
        return -1

    x = 0
    for i in range(len(arr)):
        x += (10 ** i) * int(arr[i])
    return x


res = next_smaller(51555001)
print(res)
