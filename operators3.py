# Idenity operators
var2 = "hello"
varr = "hello"
var = "hello world"
if var2 is varr:
    print("both are same")
if var2 is not varr:
    print("both are not the same")

#membership operator
var2 = "hello"
varr = "hello"
var = "hello world"
if var2 in var:
    print("both have a contain common word")
if var2 not in var:
    print("both do not contain a common word")
# Left shift and right shift - bitwise operations:
a = 5
b = 3

print("left shift <<", a<<1)
print("right shift >>", a>>1)

#revision
print("enter marks obtained in maths:")
m1 = int(input())
print("enter marks obtained in sceince:")
m2 = int(input())
print("enter marks obtained in inquiry:")
m3 = int(input())
total = m1 + m2 + m3
avg = total/3
if avg >= 91 and avg <= 100:
    print("yor grade is A1")
elif avg >=81 and avg < 91:
    print("yor grade is A1")
elif avg >= 71 and avg < 81:
    print("yor grade is b1")
elif avg >= 61 and avg < 71:
    print("yor grade is c1")
else:
    print("invalid input")