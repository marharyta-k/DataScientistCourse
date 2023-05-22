temp = float(input('Please enter the temperature: '))
measure = input('What is your measure type? Enter C for Celsius or F for Fahrenheit: ')

def c_to_f(c):
    """Convert celcius to fahrenheit and return result."""
    f = (c * 1.8) + 32
    
    return f 

def f_to_c(f):
    """Convert fahrenheit to celcius and return result/"""
    c = (f - 32) / 1.8 
    
    return c 

if measure.lower() == 'c':
    result = c_to_f(temp)
    print(f'F: {result}')
elif measure.lower() == 'f':
    result = f_to_c(temp)
    print(f'C: {result}')
else:
    print('You entered incorrect measure type')

