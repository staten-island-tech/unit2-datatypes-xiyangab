#integers and floats
""" x = 3
y = float(3) """
""" print(x,y) """

#lists
""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
 """
#what if we just want one single, specific value?
""" print(values[0])
print(values[6]) """

#string methods
""" x = "this is a thing"
y = x.split( )
z = y[0]
print(y)
print(z)
 """
#challenge
""" sentence = input("Please input any sentence.")
words = sentence.split()
print(len(words)) """

#booleans and control flow
""" day_of_week = input("what day is it?")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

#f strings
""" x = "test"
print(f"hello {x}")

temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

#challenge 1
""" x = int(input('Please input a number.'))
if x % 2 == 0:
    print('This number is even.')
else: 
    print('This number is odd.') """

#challenge 2
""" bill = int(input('Please enter the bill amount.'))
service = input('Was the service bad, okay, good, or great?')
    
if service == 'bad':
    print(bill * 0)
elif service == 'okay':
    print(bill * .15)
elif service == 'good':
    print(bill * .20)
elif service == 'great':
    print(bill * .25)
 """

#challenge 3
""" number = int(input('Type a number for all factors.'))
divisor = 1
for i in range(number):
    if number % divisor == 0:
        print(divisor)
    divisor = divisor + 1 """

#challenge 4
x = int(input('Please type the first number.'))
y = int(input('Please type the second number.'))
divisor = 1

for i in range(x):
    set1 = []
    if x % divisor == 0:
        set1.append(divisor)
    divisor = divisor + 1

divisor = 1

for i in range(y):
    set2 = []
    if y % divisor == 0:
        set2.append(divisor)
    divisor = divisor + 1

list = 0

for i in range(set1 + set2):
    if set1[list] == set2[list]:
        list = list + 1
        