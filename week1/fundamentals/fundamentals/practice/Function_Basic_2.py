def countdown(number):
 return list(range(number, -1, -1))
countdown_list = countdown(5)
print(countdown_list)

def print_and_return(numbers):
    print(numbers[0])
    return numbers[1]
numbers = [10, 20]
result = print_and_return(numbers)
print("Returned value:", result)

def First_Plus_Length(lst):
   return lst[0]+len(lst)
lst=[2,5,8,4]
print (First_Plus_Length(lst))

def Values_Greater_than_Second(list):
   new=[]
   po=list[1]
   sum=0
   if len(list)< 2:
      return False
   for i in range (0,len(list),1):
      if po < list[i]:
       sum +=1
       new.append(list[i])
   print (new)
   return sum
list = [5, 2, 9, 12]
result = Values_Greater_than_Second(list)
print("Result:", result)

def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))
    
   
