

''' We usually get input in string format.
By using eval() we can convert that string to integer'''
n = eval(input("enter the no of terms required: "))
a = 0
b =1
print(a)
print(b)
for i in range(3,n+1):
         c = a+b;
         print(c)
         a=b
         b=c
