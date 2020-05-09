def pow(x,n):
    if n == 0:
        return 1
    return x * pow(x,n-1)


print(pow(4, 0)) # 1
print(pow(1, 67)) # 1
print(pow(2, 8)) # 256
print(pow(3, 3)) # 27
