num1 = 42 # variable declaration; number initialized; 
num2 = 2.3 # varaiable declartion; number initialized; 
boolean = True # variable; boolean;
string = 'Hello World' #variable; string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable; list;
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable; dictionary; 
fruit = ('blueberry', 'strawberry', 'banana') #variable; tuples;
print(type(fruit)) # printo to console, type;
print(pizza_toppings[1]) #print to console; list value;
pizza_toppings.append('Mushrooms') #add value to list 
print(person['name']) #print to console; dictionary value
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary chane value
print(fruit[2]) # print to conosle; tuple data; 

#conditional if, print to console; conditional else, print to console; 
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#conditional if, elif, else, print to console.
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

#for loop start at 0 go to 5
for x in range(5):
    print(x)
#for loop start at 2 go to 5
for x in range(2,5):
    print(x)
#for loop start at 2 go to 10 by increments of 3
for x in range(2,10,3):
    print(x)
x = 0
#while loop declaration, print to console incrementing by 1 
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() #list delete at end
pizza_toppings.pop(1) #list delete value at index of 1 

print(person) #print to console of dictionary 
person.pop('eye_color') #delete value in dictionary 
print(person) #print to console of dictionary 

# for loop through a list of toppings 
for topping in pizza_toppings:
    #conditional if 'pepperoni' 
    if topping == 'Pepperoni':
        #proceed 
        continue
    #print to conolse 
    print('After 1st if statement')
    #conditional if 'olives'
    if topping == 'Olives':
        #for loop terminated 
        break

#fucntion declartion 
def print_hello_ten_times():
    #for loop starts at 0 goes up until 10 
    for num in range(10):
        #print to console 'hello' 
        print('Hello')

print_hello_ten_times() #calling the function 

#fucntion declartion with parameter x
def print_hello_x_times(x):
    #for loop until given number x
    for num in range(x):
        #print to conosle 
        print('Hello')

print_hello_x_times(4) #calling fucntion of 4 

#fucntion declaration w/ parameter 
def print_hello_x_or_ten_times(x = 10):
    #for loop until x 
    for num in range(x):
        #print to conosle 
        print('Hello')

print_hello_x_or_ten_times() #fucntion call goes to 10
print_hello_x_or_ten_times(4) #function call goes to 4 


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)