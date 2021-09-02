Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20;a+=30;a%=3;
>>> print(a)
2
>>> True * False
0
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True==False) or (False > True))and(False<=True)
False
>>> s1="Nice to have it"
>>> s2="here"
>>> s1+s2
'Nice to have ithere'
>>> print(s1+' '+s2)
Nice to have it here
>>>
#4
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])

#5
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
s1="Nice to have it"
s2="here"
a.insert(0,s1)
a.append(s2)
print(a)

#6
numbers=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,958,743,577]
for i in numbers:
  if i==237:
    break
  else:
    if i%2==0:
      print(i)

#7
colour_list_1=set(["White","Black","Red"])
colour_list_2=set(["Red","Green"])
print(colour_list_1-colour_list_2)

#8
s=input()
a=set('abcdefghijklmnopqrstuvwxyz')
if a<=set(s.lower()):
  print("string is pangram")
else:
  print("string is not pangram")

#11
n=input().split(',')
items=[i for i in n]
items.sort()
print(','.join(items))

#13
n=input()
count=0
count1=0
for i in n:
  if i.isdigit():
    count=count+1
  elif i.isalpha():
    count1=count1+1
  else:
    pass
print("Letter",count1)
print("Digit",count)
  
      
