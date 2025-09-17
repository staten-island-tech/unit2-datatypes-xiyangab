# strings represent characters or text
""" x = "Dang it Yi" """
# inputs output strings
""" name = input("What's your name")
print(name)
def add(x,y): """
    # will print this out after you msg
"""     return x + y
z = add(5,15)
print(z)   """

#integers or numbers
""" a = int('5')
bill = input("How much was the bill?")
print(int(bill) * .15) """

""" name = "Mason"
#use F string
print(f"His name is {name}") """

#Float
#bill = 3.14

""" students = ["Cadee", "Mason", "Andy"] """
#can reference each item in a list by their index
""" print(students[0])#prints cadee """

#add student
""" students.append("Alina") """

#we can iterate or loop through a list
""" for student in students:
    print(student) """

#BooLean true of false
""" x = True
y = False """
# evaluations use double ==
""" if x == True:
    print("Hello Robby")
else:
    print("Goodbye Rodney") """

#evaluation in lists
""" students = ["Cadee", "Mason", "Abby"]
if "Alina" in students:
    print("She's here")
else:
    students.append("Alina")
    print("We added Alina") """
"""  """
""" x = 91
if x <10: 
    print("Less")
elif x == 10:
    print("Equal")
else:
    print("Greater than 10") """

""" students = ["Cadee", "Mason", "Abby"]
for student in students:
    found = False
    if student == "Mason":
        print("Found Mason")
        found = True """

""" name= "Cadee"
#print (name[0])
for letter in name:
    print(letter) """

""" x = ["This", "Sentence"] """
#len = length
""" print(len("This Sentence")) """

friend_comes = True
money = True

""" def and_movies(friend, money): """
    #dont need to add "== True"
"""     if friend == True and money == True:
        print("Going to the movies")
    else:
        print("I have no friends or i have no money")
and_movies(friend_comes, money) """

""" def or_movies(friend, money):
    if friend or money:
        print("Going to the movies")
    else:
        print("I have no friends and i have no money")
or_movies(friend_comes, money) """

""" homework = True
def not_movies(homework):
    if not homework:
        print("move time")
    else:
        print("homework time, i hate russian")
not_movies(homework)
 """

#prints the remainder
""" print(5 % 3) """

""" def factor(x,y):
    if x % y == 0:
        print("Y us a factor of {x}") """