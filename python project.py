#Roman to integer

def rti(s):
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
               'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} 
      i = 0
      n = 0
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in roman:
            n+=roman[s[i:i+2]]
            i+=2
         else:
            #print(i)
            n+=roman[s[i]]
            i+=1
      return n
x=input("Enter an number in Roman Number: ")
print("Value in decimal is %d"%rti(x))


















































        
























