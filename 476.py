"""<---------------------program 1 for palindrome----------------->"""

#1. Implement palindrome using iterator(for loop) and generator mechanism.

pal="1214"
pal2=""
#<--------------for loop--------------->
for i in pal:
    pal2=i+pal2
if pal==pal2:
    print("given number is palindrome")
else:
    print("given number is not palindrome")

    """i in the above program thenloop iterates the value 
    and store that value in new string pal2. After that the if statement
    is checks the condition if it is true it retuens the print statement
    on the if condition body if it false the else body will be printed"""
#<-----------generator-------------------->
pal3=""
pal='1214'

def palindrome(pal):
    for i in pal[::-1]:
        yield i
for i in palindrome(pal):
    pal3+=i
if pal3==pal:
    print("palindrome")
else:
    print("not palindrome")
palindrome(pal)

#<------------------programe 2  add two integer value by position------------------->


"""2. Sum of 2 digits into output
		n1 = 1234 # int(input("Enter number1 :" ))
		n2 = 9999 # int(input("Enter number2 :" ))
		Output: 9+1 2+9 3+9 4+9 
		         10 + 11 + 12 + 13
				 46"""

n1 = 1234
n2 = 9999
st1=str(n1)
str2=str(n2)
l1=list((st1))
l2=list((str2))
l3=[]
for i in range(len(st1)):
    x=int(l1[i])+int(l2[i])
    l3.append(x)
output=int()
for i in l3:
    output+=i
print("the finalu output of n1,n2:",output)

""" in the above program we know that inter value are not possible 
for indexing so that reason first we can convert the int into str after that
we can convert the str  value into list. By using indexing we can add the 
value in the list after that we convert the list of value into inter value
"""


#<-------------------programme 3 ------------------>

""" st = "ab@#cd!ef"
   Reverse string considering only alphabets. Symobls should not be reversed
   # Output: fe@#dc!ba"""




#<-------------------------  program4---  count the the duplicate values------------->
#4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
   #findout elements duplicate count output in  dict format
list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
str=""
'''iterating the loop for list'''
for i in list:
    #adding values to empty stringn 'str'
    str+=i
dict={}
#creating empty dictionary
for i in str:
    '''adding values to empty dictionary'''
    dict[i]=str.count(i)
print(dict)


#<------------------------------------------program 5 add two tuples  ------------------------->
#5.  # t1 = (1, 2, 3, "a", "c")
# t2 = ("b", "d", 9, 8, 7)
# Output: (10,10,10,"ab","cd")'''
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
result = []
x = []
y = []
r = []
''''add the integer value in to one list x and string into y and than add x+y store the value in z'''
for i in list(t2):
    if type(i) == int:
        x.append(i)
    else:
        y.append(i)

z = x + y
''' add the value from list and z by using index '''

for i in range(len(t1)):
    a = list(t1)
    b = a[i] + z[i]
    r.append(b)
result = tuple(r)
print(result)
#<-----------programme 6 ----------------->
''' removing 0's in a string'''
inp = "216.08.094.196"
inp2=""
# o/p =  216.8.94.196
for i in inp:
    if i=='0':
        continue
    inp2+=i
print(inp2)


'''<-----------program 7----------->'''
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# output= [1,2,3,4,5,6,7,8,9,10]
#add values to empty list l2 by using extend and append
l2=[]
for i in l:
    if type(i)==list:
        l2.extend(i)
    else:
        l2.append(i)
#add values to empty list l4 by using extend and append
l4=[]
for i in l2:
    if type(i)==list:
        l4.extend(i)
    else:
        l4.append(i)
print(l4)







