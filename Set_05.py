# S05Q01:Print the multiplication table of a given number using “for” and “while” loops.
num = int(input("Enter the number:"))
for n in range(1, 11):
    print(num, "*", n, "=", num*n)
    
# using while loop

count = 0
while count < 10:
    count += 1
    print(count * num)

#S05Q02: Ask the user to enter a number till he enters 0.Print the maximum and minimum values among all entered numbers.Print the number of single, two and three digit numbers entered.
max_num = float('-inf')
min_num = float('inf')
single_digit_count = 0
two_digit_count = 0
three_digit_count = 0

while True:
    num = int(input("Enter the number(not 0):"))
    if num == 0:
        break
    max_num = max(max_num, num)
    min_num = min(min_num, num)
    
    num_length = len(str(abs(num)))
    if num_length == 1:
        single_digit_count += 1
    elif num_length == 2:
        two_digit_count += 1
    elif num_length == 3:
        three_digit_count += 1
print("max_num=", max_num)
print("min_num=", min_num)
print("single_digit_count=", single_digit_count)
print("two_digit_count=", two_digit_count)
print("three_digit_count=", three_digit_count)

# S05Q03:Take a number as input from the user.Print all the squares of numbers from 1 to any large number.The numbers printed should be less than the number given as input by the user

num = int(input("enter the number:", ))
count = 1


while (count ** 2) < num:
	print(count ** 2)
	count += 1
print("The End")

# S05Q04:Check if a given number is a fibonacci number.If not, then print the closest fibonacci number to the given number	



