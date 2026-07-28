# define a function to add two numbers
# def add_numbers(a,b):

#   result = a + b
#   return result

#print(add_numbers)



"""
Lambda function is a small, anonymous
function-ofter written in one line
syntax
===============
lambda arguments : expression

"""
# write a lambda that returns addition

add_num = lambda num_1,num_2:num_1 + num_2
print(add_num(2,3))


#write a lambda that returns the square of a number

num_square = lambda num_1: num_1 ** 2
print(num_square(5))


# Create a lambda that returns
#"pass" if marks are 40 or above :otherwise "Fail"

marks = lambda mark:"pass"if mark >= 40 else"fail"
print(marks(56))



#define 
num =[10,15,20,30,45,50,60]
result = lambda num:[i for i in num if i % 3 == 0 and i % 5 ==0 ]
print(result(num))



# define a function palindrome from a list of words
words = ["madam","python","level","code","radar"]
palindrome = lambda words:[i for i in words if i == i[::-1]]
print(palindrome(words))


# define a function to check the number is positive or negative
result = lambda num:"positive"if num > 0  else("negative" if num < 0 else "negative")
print(result(55))




