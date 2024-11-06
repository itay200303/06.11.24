# 1.
top: int = int(input("enter a natural num: "))
if top > 0:
    for i in range(1, top + 1, 1):
        print(i)
else:
    print("put a  natural num")

# 2.
salem1: int = int(input("enter a natural num: "))
salem2: int = int(input("enter a natural num: "))
beginner = min(salem1, salem2)
ending = max(salem1, salem2)
for num in range(beginner, ending + 1):
    print(num)

# 3.
n: int = int(input("enter a num: "))
for i in range(0, n + 1, +2):
     print(i, end=" ")

# 4.
max1: int = int(input("enter a num: "))
den: int = int(input("enter a num: "))
for i in range(1, max1 + 1):
    if i % den == 0:
        print(i)



