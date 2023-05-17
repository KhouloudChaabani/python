# for i in range(151):
#  print(i)
# for i in range(5, 1001, 5):
#  print(i)
for i in range(1, 101):
 if i % 10 == 0:
    print("Coding Dojo")
 elif i % 5 == 0:
    print("Coding")
 else:
    print(i)
    total_sum = 0

for i in range(1, 500001, 2):
    total_sum += i
print("The sum of odd integers from 0 to 500,000 is:", total_sum)
number = 2018
while number > 0:
    print(number)
    number -= 4
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)