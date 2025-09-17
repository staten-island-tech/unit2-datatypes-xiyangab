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
number = input('Please input any number.')
def odd():
    if not number % 2 == 0:
        print('This number is odd.')
    else:
        print('This number is even.')
