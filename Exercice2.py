def reverseString(s, i = 0) :
   """Reverses the string s recursively """
   if i == len(s):
       return ""
   return reverseString(s, i+1)+ s[i]

print(reverseString(" ")) # " "
print(reverseString("je suis en python")) #nohtyp ne sius ej
print(reverseString("radar")) # radar
