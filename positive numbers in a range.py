
''' We usually get input in string format.
By using eval() we can convert that string to integer'''


print("enter the numbers seperated by a comma and enclosed within square brackets")
list = eval(input("enter elements: "))
list2 = []


# if the number is positive then it will be appended to list2
for x in range(0,len(list)):
    if list[x]>0:
        list2.append(list[x])
print(list2)
