a = "hello"
b = "b2"
c = "333      "

d = a + "   " +  b  +  "   " +  c


print(d)

print(len(d))

print(d[ :-3])
print(d[ ::-1])

print(d.upper())

print(d.lower())

print(d.strip())


print(d.split(" d"))


print(d.capitalize)

print(d.find("b2"))

print(d.find("a2"))

print(d.nu)



a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))

# Perform arithmetic operations
sum = a + b
sub = a - b
mul = a * b
div = a / b

# Print results
print("Sum:", sum)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)

a="hello"
b="b2"
c="333"

d = a + " " + b + " " + c
print(d)
print(len(d))
print(d[:-3])
print(d[::-1])
print(d.upper())
print(d.lower())
print(d.strip())
print(d.title())
print(d.lower())
print(d.title())
print(d.strip())
print(d.isdigit())
print(d.find("b2"))
print(d.find("a2"))
print(d.capitalize())
print(d.isnumeric())
print(d.count("3"))
print(d.split())
print(d.replace("hello", "python"))
print(d.swapcase())


#d)if "a2" in d:
if "a2" in d:



    
    print("Yes")
else :
    print("No")



x = lambda a, b: a + b


a = int(input("Enter "))
b = int(input("Enter "))


print("Result:",x(a,b))


a = [1,2,3,9,5,8,7]

b = [x for x in a if x%2==0]
print(b)