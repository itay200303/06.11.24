# 1.
sum_num = 0
while True:
    numbers: int = int(input("enter a num: "))
    if numbers == -99:
        break
    sum_num += numbers
    print(sum_num)
print(None)

# 2.
max_number: int = None
min_number: int = None
while True:
    num : int = int(input("enter a num: "))
    if num == -99:
        break
    if num <= 0:
        break
    if max_number is None or num > max_number:
        max_number = num
    if min_number is None or num < min_number:
        min_number = num
print(None)
print(f"maximum number is {max_number}")
print(f"minimum number is {min_number}")

# 3.
numbers = []
for i in range(5):
    num: int = int(input("Enter a num: "))
    numbers.append(num)
max_number = max(numbers)
max_index = numbers.index(max_number)
print(f"the biggest number is : {max_index}")

# 4.
num_kepel1: int = int(input("Enter a num: "))
num_kepel2: int = int(input("Enter a num: "))
sum_kepel = 0
for _ in range(num_kepel2):
    sum_kepel += num_kepel1
if num_kepel2 < 0:
    sum_kepel = -sum_kepel
print(sum_kepel)

# 5.
num_hezka1: int = int(input("Enter a num: "))
num_hezka2: int = int(input("Enter a num: "))
sum_hazka = 0
for _ in range(num_hezka2):
     sum_hazka *= num_hezka1
if num_hezka2 < 0:
    sum_hazka = 1 / sum_hazka
print(sum_hazka)

# 6
# will do as homework

# 7
# will do as homework

# 8
# will do as homework






