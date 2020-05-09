def listSum(l):
    if len(l) == 0:
        return 0
    return listSum(l[1:]) + l[0]


print(listSum([])) # 0
print(listSum([12])) # 12
print(listSum([35,18,0,4,9,8])) #74
