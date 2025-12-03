# we have to count a vowel in this given str
# s1="Python Coding Is Awesome"
# o=0
# c=0
# for i in s1:
#     if i==" ":
#         continue
#     elif i in "aeiouAEIOU":
#         o +=1
#     else:
#         c +=1
# print("total vowels->",o) 
# print("total consonents->",c)


# program to count the total number of uppercase and lowercase charaters
# s1="SuperCaliFragilisticExpilodicous"
# u=0
# l=0
# for i in s1:
#     if i>='a' and i<='z':
#       l+=1
#     elif i>='A' and i<='Z':
#        u+=1
 
# print("uppercase count:",u)
# print("lowercase count:",l)          


#convert all lowercase to uppercase character and uppercase to lowercase
# s1="SuperCaliFragilisticExpilodicous"
# s2=""
# print(s1)
# for i in s1:
#     if i>='a' and i<='z':
#         s2+=chr(ord(i)-32)
#     elif i>='A' and i<="Z":
#         s2+=chr(ord(i)+32)

# print(s2)           


# write a program to convert camel case into snake case character
# camel case means have a space in a given str
# snake case means that space in a given str that convert or replace with the underscore and covert the character into lowercase
# s1="Dont Be A Stupid Be An Idiot"
# s2= ""
# print(s1)
# for i in s1:
#     if i==' ':
#         s2+='_'
#     elif i>='A' and i<="Z":
#         s2+=chr(ord(i)+32)
#     else:
#         s2+=i    
# print(s2)
# #this is for change the lower to upper   
# s3="" 
# for i in s1:
#     if i==' ':
#         s3+='_'
#     elif i>='a' and i<="b":
#         s3+=chr(ord(i)-32)
#     else:
#         s3+=i
# print(s3)         

# this is change l to u and u to l and camel to snake
# s1="Dont Be A Stupid Be An Idiot"
# s2=""
# print(s1)
# for i in s1:
#     if i==" ":
#         s2+='_'
#     elif i>='a' and i<='z':
#         s2+=chr(ord(i)-32)
#     elif i>='A' and i<="Z":
#         s2+=chr(ord(i)+32)
#     else:
#         s2+=i
# print(s2)        


# snake to camel
# s1="dont_be_a_stupid_be_an_idiot"
# s2=""
# print(s1)
# s2+=chr(ord(s1[0])-32)
# for i in range(1,len(s1)):
#     if s1[i]=="_":
#         s2+=' '
#     elif s1[i-1]=="_":#to check current character's previous character is _ or not
#         s2+=chr(ord(s1[i])-32)
#     else:
#         s2+=s1[i]        

# print(s2)       

# program to check given str is a palindrome str or not
# s1="madam"
# s2=s1[::-1]
# if s1==s2:
#     print("it is a palindrome")
# else:
#     print("not a palindrome") 

# or
# using for iteration
# s1="madam"
# j=len(s1)-1
# for i in range(len(s1)):
#     if s1[i]!=s1[j]:
#         print("not a palindrome")
#         break
#     j-=1
# else:
#     print("It is a palindrome")    


# find the frequency of each character in the given str
# charcter present in given str output like i-3,f-1 etc...
# s1="if you always do what you always did you will always get what you always got"
# s2={}
# for i in s1:
#     if i not in s2:
#         s2[i]=1
#     else:
#         s2[i]+=1
# for i,j in s2.items():
#     print(i,"->",j)



# 
#first string first element second string last element
# s1='abcd'
# s2='wxyz'
# s3=''
# j=len(s2)-1
# for i in range(len(s1)):
#     s3+=s1[i]+s2[j] # s3+=s1[i]+s2[len(s2)-i-1]
#     j-=1
# print(s3)



# middle char insertion
s1='rishab'
s2='pant'
s3=''
mid=len(s1)//2
for i in  range(len(s1)):
    if i==mid:
        s3+=s2+s1[i]
    else:
        s3+=s1[i]
print(s3)



# if the special char count is even we have to reverse else we have to append same
# s1="I@@# Am!!@@## Pool@#$ Deadpool##$%^& Here!@# TO&&!!@# Kill!@#$%^ Bad#$%  Guys!@#$%&"
# s2=s1.split()
# s3=''
# for i in s2:
#     cnt=0
#     for j in i:
#         if j>='A' and j<='Z' or j>='a' and j<='z':
#             continue
#         else:
#             cnt+=1
#     if cnt%2==0:
#         s3+=i[::-1]+' '
#     else:
#         s3+=i+' '
# print(s3)


# wap to check the given strings are anagram strings or not
# s1='night'
# s2='thing'
# n=1
# for i in s1:
#   if i in s2:
#     n*=1
#   else:
#    n*=0
# if n==1:
#   print('anagram')
# else:
#   print('not')

# or

# def sort(s):
#   s=list(s)
#   for i in range(len(s)):
#     for j in range(i+1,len(s)):
#       if s[i]>s[j]:
#         s[i],s[j]=s[j],s[i]
#   return "".join(s)
# if sort(s1)==sort(s2):
#   print('yes')
# else:
#   print("not")


# check the string is panagram string or not
# s='Pack My Box with five dozen liquor jugs'
# s1=set()
# for i in s:
#     if i==" ":
#         continue
#     else:
#         s1.add(i.lower())
# if len(s1)==26:
#     print('panagram')
# else:
#     print("not")


# 21/11/25

# WAP to check given string can be a mirror string or not
# The mirror characters are...A H I M O T U V W X Y and the numbers are 0 8.
# def mirror_string(s):
#     mirror_char={'A','H','I','M','O','T','U','V','W','X','0','8'}
#     for i in s:
#         if i.upper() not in mirror_char:
#             return False
#     return s

# s1="AHA"
# if mirror_string(s1):
#     print("Mirror string")
# else:
#     print("Not a mirror string") 



# WAP to find how many different words are there in the given string and with their index values in the form of the list
# Output If:[0], you:[1,5,8,13], always:[2,6,10,14], do:[3], what:[4,12], did:[7], will:[9], get:[11], got:[15]
# s1="If you always do what you always did you will always get what you always got"
# s2=s1.split()
# d1={}
# for i in range(len(s2)):
#     if s2[i] not in d1:
#         d1[s2[i]] = [i]
#     else:
#         d1[s2[i]]+=[i]
# for k,v in d1.items():
#     print(k,":",v)



# WAP to check the given input string can be a strong password or not
# It should contains minimum 8 characters and maximum 30 characters
# It should contains atleast one uppercase, one lowercase, one numeric and one special character
# If it is not satisfing the above criteria display the message accordingly
# And check the string should not starts with the numeric values.
# s1=input("Enter the password: ")
# lc,uc,sc,nc = 0,0,0,0
# if len(s1)>=8 or len(s1)<=30:
#     if ord(s1[0])>=48 and ord(s1[0])<=57:
#         print("String should not starts with number")
#     else:
#         for i in range(len(s1)):
#             if s1[i]>='a' and s1[i]<='z':
#                 lc+=1
#             elif s1[i]>='A' and s1[i]<='Z':
#                 uc+=1
#             elif s1[i]>='0' and s1[i]<='9':
#                 nc+=1
#             else:
#                 sc+=1
#         if lc>=1 and uc>=1 and nc>=1 and sc>=1:
#             print("It can be a atrong password")
#         else:
#             print("It can't be a strong password")
# else:
#     print("Password should contains minimum 8 characters and maximum 30 characters")



# Assignment
# input --> s1="pneumonultramicroscopicsilicvolcanoconosis it refers to the lungs disease caused by silica dust"
# Output-->(remove all the spaces) and if the input is 5 then 1st 5 characters in first line, next 5 characters in second line and so on
# import math
# s1="pneumonultramicroscopicsilicvolcanoconosis it refers to the lungs disease caused by silica dust"
# s2=""
# for i in s1:
#     if i == " ":
#         continue
#     else:
#         s2 += i
# s3=""
# div = math.ceil(math.sqrt(len(s2)))
# cnt = 0
# for i in s2:
#     if cnt == div:
#         s3 += "\n"
#         cnt = 0    
#     s3 += i
#     cnt += 1
# print(s3)



# 24/11/25

# WAP to convert the given string into a modified string based on the given conditions.
# Check the length of the string. If it is even check ascii value of each character if ascii value is even add +4 to it and again convert it into an ascii character 
# If character's ascii value is odd add +3 to it and convert it into respective ascii character.
# If the length is odd add +6 to even ascii value and add +5 to odd ascii value.
# s1="python"
# s2=""
# if len(s1) % 2 == 0:
#     for i in s1:
#         if ord(i) % 2 == 0:
#             s2 += chr(ord(i)+4)
#         else:
#             s2 += chr(ord(i)+3)
# else:
#     for i in s1:
#         if ord(i) % 2 == 0:
#             s2 += chr(ord(i)+6)
#         else:
#             s2 += chr(ord(i)+3)
# print(s2)



# WAP to compress the given string to get the decide output
# s1="aaaabbccccccddddeeeefggggg"
# s2=""
# cnt=1
# for i in range(len(s1)-1):
#     if s1[i]==s1[i+1]:
#         cnt+=1
#     else:
#         s2+=s1[i]+str(cnt)
#         cnt=1
# s2+=s1[len(s1)-1]+str(cnt)
# print(s2)



# If the length of the string is odd then the output should be
#         p
#         y
#         s
#         p
# P y s p i d e r s
#         d
#         e
#         r
#         s
# If the length of the string is even then print our name same as the above pattern
# s1="Pyspiders"
# if len(s1)%2 != 0:
#     for i in range(len(s1)):
#         for j in range(len(s1)):
#             if i == len(s1)//2:
#                 print(s1[j],end=" ")
#             elif j == len(s1)//2:
#                 print(s1[i],end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
# else:
#     print("Output will work for only odd length string")



# Assignment
# No need to check the length of the string
# 1.output --> 
#       p
#     y s p
#   i d e r s 
# p y s p i d e
# 2. output --> print also based on user input 
# s1="Pyspiders"
# n=int(input("n :"))
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(s1[k],end=" ")
#     print()




# 25/11/25

# WAP to print the pattern using user inputs string and a integer.
# Ex: int --> n=5
#     str --> s1="pyspiders"
# output
# p y s p i
# d e r s p
# y s p i d
# e r s p y
# s p i d e
# s1="pyspiders"
# n=int(input("n:"))
# val=0
# if n > 2:
#     for row in range(n):
#         for col in range(n):
#             print(s1[val],end=' ')
#             val += 1
#             if val == len(s1):
#                 val = 0
#         print()
# else:
#     print("Enter value greater then 2")



# check the given count of substring is present in the original string or not
# Output --> no of times present(number)
# s1="abcdaaabbcdaabcdabcd"
# s2="bcd"
# s3={}
# for i in range(len(s1)):
#     if s1[i:i+len(s2)] == s2:
#         if s1[i:i+len(s2)] in s3:
#             s3[s1[i:i+len(s2)]] += 1
#         else:
#             s3[s1[i:i+len(s2)]] = 1
# for k,v in s3.items():
#     print(k,":",v)

# Or

# s1="abcdaaabbcdaabcdabcd"
# s2="bcd"
# cnt = 0
# for i in range(len(s1)):
#     if s1[i:i+len(s2)] == s2:
#         cnt += 1
# print("Count of Substring :",cnt)



# input = "The most violent man called one man the most violent"
# output --> In each word the number of vowel and the number of consonent in a list
# Ex: The - [1,2]
#     most - [1,3]
#     violent - [3,4]
#     man -[1,2]
#     called -[2,4]
#     one -[2,1]
#     the -[1,2]
# s1 = "The most violent man called one man the most violent"
# s2 = s1.split()
# d1 = {}
# for i in s2:
#     v = 0
#     c = 0
#     for j in i:
#         if j in "aeiouAEIOU":
#             v += 1
#         else:
#             c += 1
#     if i not in d1:
#         d1[i] = [v,c]
# for i,j in d1.items():
#     print(i,":",j)



# Assignment
# WAP to print all possible substrings from the given string
# input --> "abcd"
# output --> a
#            a
#            ab
#            abc
#            abcd
#            b
#            bc
#            bcd
#            c
#            cd
#            d
# s1="abcd"
# for i in range(len(s1)):
#     for j in range(i+1,len(s1)+1):
#         print(s1[i:j])




# WAP to group all the anagram strings into a single list
# input --> ['tan','ant','bat','eat','nat','ate','tab']
# output --> [['tan','ant','nat'],['bat','tab'],['eat','ate']]
# s1=['tan','ant','bat','eat','nat','ate','tab']
# d1={}
# s2=[]
# for i in s1:
#     s2=''.join(sorted(i))
#     if s2 in d1:
#         d1[s2].append(i)
#     else:
#         d1[s2]=[i]
# for i,j in d1.items():
#     print(list(d1.values()))
    # break

# wap to make the sum of only integer values present in the dictionary

# d1={
#   "a":"one",
#   2:100,
#   "one":"five",
#   3:"python",
#   5:65,
#   "r":"spy",
#   6:12
# }
# sum=0
# for i in d1.values():
#   if type(i)==int:
#     sum+=i
# print(sum)
# OR

# res=0
# for k, v in d1.items():
#   if type(v)==int:
#     res+=1
# print(res)

# wap to encode and decode the numeric string based on the morse code
# when the programme is executed it should ask 2 options 1st one encode and 2nd one decode
# if it is encode it should accept numeric string convert to marks code values
# if it is decode need to except marsecode as input and convert to numeric string
# morse_code={
# 0:"- - - - -",
# 1:". - - - -",
# 2:". . - - -",
# 3:". . . - -",
# 4:". . . . -",
# 5:"- - - - -",
# 6:"- . . . .",
# 7:"- - . . .",
# 8:"- - - . .",
# 9:"- - - - ."
# } 
# def encode_morse_code(num_str):
#   encoded=""
#   for i in num_str:
#     if ord(i)>=48 and ord(i)<=57:
#       encoded+=morse_code[i]
#     return encoded
  
# def decode_morse_code(morsecode):
#   reverse_morse_code={code:digit for digit,code in morse_code.items()}
#   new=morsecode.split()
#   decode=""
#   for i in new:
#     if len(i)==5:
#       decode+=reverse_morse_code[i]
#     else:
#       return "make sure marse code contains only 5 characters only"
#   return decode
# print("morse code converter")
# print("1.Encode\n 2.decode")
# opt=int(input("enter your option"))
# match opt:
#   case 1:
#     num_str=input("Enter only digits")
#     print(encode_morse_code(num_str))
#   case 2:
#         print("enter marse code with space and each marse code should have 5char")
#         code=input("enter the marse code:")
#         print(decode_morse_code(code))
#   case _:
#     print("invalid")

# wap to build a vending machine, it should contain a dictionary of product along with its price
# create a class for vending machine during the object creation it should accept dictionary of products
# it should contains a methods like add cart,display cart,update cart and the bill summary
# Products={
#   "cupcake":10,
#   "kitkat":20,
#   "oreo": 25,
#   "chikki":5,
#   "mazza":15,
#   "pepsi": 30
# }
# class vending_Machine:
#   def __init__(self,**products):
#     self.products=products
#     self.cart={}

#   def add_cart(self):
#     pass
#   def display_cart(self):
#     pass
#   def update_cart(self):
#     pass
# cv



