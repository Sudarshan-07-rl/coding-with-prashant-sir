num = 123 #321
print("Original number is: ", num)
a = num % 10 #3
num = num // 10 #12
b = num % 10 #2
num = num // 10 #1
c = num % 10 #1
rev = a*100 + b*10 + c*1
print("Reverse of the number is: ", rev)

num =123456
print("Original number is: ", num)
p = num % 10 #6
num = num // 10 #12345
q = num % 10 #5
num = num // 10 #1234
r = num % 10 #4
num = num // 10 #123
s = num % 10 #3
num = num // 10 #12 
t = num % 10 #2
num = num // 10 #1
u = num % 10 #1
rev = p*100000 + q*10000 + r*1000 + s*100 + t*10 + u*1
print("Reverse of the number is: ", rev)