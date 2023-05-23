N = int(input('Please enter your number: '))

#1
def square(N):
    sq_list = []
    for i in range(N):
        sq_list.append(i**2)
    return sq_list

result1 = square(N)
print(f'Result 1: {result1}') 


#2
numbers = list(range(N))
def square(item):
    return item**2

result2 = list(map(square, numbers))
# list(map(lambda item: item**2, numbers))
print(f'Result 2: {result2}')


#3 list comprehension
result3 = [i**2 for i in range(N)]
print(f'Result 3: {result3}')

#4
def check_square(item):
    root = item**0.5
    return root.is_integer()

result4 = list(filter(check_square, numbers))
print(f'Result 4: {result4}')

#5 перевірятиме належність числа N до відрізку [a, b]
# a = int(input('Please input start of interval: '))
# b = int(input('Please input end of interval: '))
check_interval = lambda N, a, b: a <= N <= b 

# if check_interval(N):
#     print(f'Yes, your number is between {a} and {b}')
# else:
#     print(f'No, your number is not between {a} and {b}')