def nCr(n:int,r:int):
    result = 1
    for i in range(0,r):
        result = result*(n-i)
        result = result/(i+1)
    return int(result)

# print(nCr(9,3))

n,r = map(int,input().split(','))
print(nCr(n,r))
