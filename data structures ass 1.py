
#Task-1

rad = input("input radius of the circle: ")
rad = float(rad)
pi = 3.14159
area = pi*rad*rad
print("The area of the circle with radius", rad , "is", area)




#Task - 2

print("\n\n\n")
fn= input("Enter Filename: ")
#splitting the file name wherever "." is found
f = fn.split(".")
""" we are printing f[-1] because, we know that the last word is the file extension
 because there might be chances where we can have "." in the file name itself.
so it is safe to use f[-1] than f[1]"""
print ("Extension of the file is : " + f[-1])
