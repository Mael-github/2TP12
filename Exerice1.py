def modulo(x, y) :
   """Computes x % y recursively """
   if (x / y) < 1:
       return x
   else:
       return modulo(x - y, y)

print(modulo(8, 16)) #8
print(modulo(45, 10)) #5
print(modulo(24, 2)) #0
print(modulo(64, 5)) #4
