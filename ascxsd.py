n = int(input("enter value of n: "))
result = 0
for i in range(1, n):
    result = result + i/((i+1)**2)
print(result)
