x = [1,15,25,38,8]
a = []

index = 0
b = 0
while index < len(x) :
    b = x[index] + b
    a.append(b)
    index += 1
print(a)
