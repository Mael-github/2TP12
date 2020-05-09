def product(a,b):
    if b == 0:
        return 0
    return product(a,b-1) + a

print(product(1,2)) # 2
print(product(3,4)) # 12
print(product(5,6)) #30
