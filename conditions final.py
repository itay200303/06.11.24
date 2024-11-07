# 1.
num_1: float = float(input("enter a num: "))
num_2: float = float(input("enter a num: "))
if num_1 > num_2:
    print(num_2)
    print(num_2)
    print(num_2)
else:
    print(num_1)
    print(num_1)
    print(num_1)

# 2.
num_int1: int = int(input("enter a num: "))
num_int2: int = int(input("enter a num: "))
print((num_int1 + num_int2) // 2 )

# 3.
num1: int = int(input("enter a num: "))
num2: int = int(input("enter a num: "))
num3: int = int(input("enter a num: "))
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

# 4.
length_movie: int = int(input("enter a num: "))
hours = length_movie // 60
minutes = length_movie % 60
print(f"the length of the movie is: {hours} hours and {minutes} minutes")

# 5.
num: int = int(input("enter a 4 digit number: "))
right_digit = num % 10
print(int(right_digit))


# 6.
num: int = int(input("enter a 4 digit number: "))
second_right_digit = num % 100 / 10
print(int(second_right_digit))

# 7.
two_digit_num: int = int(input("enter a num: "))
ahadot = two_digit_num // 10
asarot = two_digit_num % 10
sum_two_digits = asarot + ahadot
print(sum_two_digits)

# 8.
num_int: int = int(input("enter a num: "))
ahadot: int = num_int % 10
asarot: int = num_int // 10
num_numbers: int = ahadot * 10 + asarot * 1
print(num_numbers)

# 9.
num_zugi_ezugi: int = int(input("enter a num: "))
if num_zugi_ezugi // 2:
    print("zugi")
else:
    print("ezugi")

# 10.
tax: int = 0
salary = float(input("enter your salary: "))
if salary > 6000:
    tax += (salary - 6000) * 0.10
if salary > 12000:
    tax += (salary - 12000) * 0.20
    salary = 12000
if salary > 18000:
    tax += (salary - 18000) * 0.30
    salary = 18000
if salary > 25000:
    tax += (salary - 25000) * 0.40
    salary = 25000
if salary > 35000:
    tax += (salary - 35000) * 0.45
    salary = 35000
if salary > 50000:
    tax += (salary - 50000) * 0.51
    salary = 50000
if salary < 0:
    print("salary cant be negative")
else:
    print(f"the tax that you need to pay : {tax:.2f}")
# 11.
age: int = int(input("enter a num: "))
height: int = int(input("enter a height: "))
if (8 < age < 18 and height > 115) or (age > 18 and height > 100):
    print("you can pass")
else:
    print("you dont have the right conditions to pass")






