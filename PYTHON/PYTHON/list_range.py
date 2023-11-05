
# Range(start,end,step)


for value in range(1,5):
    print(value)


numbers = list(range(1,6))
print(numbers)


even_numbers = list(range(2,11,2)) 
print(even_numbers)


squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

squ : list[str] = [1,3,5,765,44523,3434,56,45,4,45,45,4,54,5,45,4,5,45,4,5,]

min(squ)

max(squ)

sum(squ)